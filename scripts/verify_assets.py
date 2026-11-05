"""Verify the distributed An An files without third-party dependencies."""
import hashlib
import json
import struct
from pathlib import Path


def verify(root):
    sizes = {'assets/anan.png': (1536, 2288)}
    checksums = {}
    for line in (root / 'SHA256SUMS').read_text(encoding='utf-8').splitlines():
        digest, name = line.split('  ', 1)
        checksums[name] = digest
    for name, expected_size in sizes.items():
        data = (root / name).read_bytes()
        if data[:8] != b'\x89PNG\r\n\x1a\n' or data[12:16] != b'IHDR':
            raise ValueError(f'{name}: invalid PNG header')
        if struct.unpack('>II', data[16:24]) != expected_size:
            raise ValueError(f'{name}: unexpected dimensions')
        if data[25] != 6:
            raise ValueError(f'{name}: expected RGBA color type')
        if hashlib.sha256(data).hexdigest() != checksums[name]:
            raise ValueError(f'{name}: SHA-256 mismatch')
        print(f'OK: {name} ({expected_size[0]} x {expected_size[1]})')
    metadata = json.loads((root / 'animation.json').read_text(encoding='utf-8'))
    expected_frames = [6, 8, 8, 4, 5, 8, 6, 6, 6]
    if [row['frames'] for row in metadata['animation_rows']] != expected_frames:
        raise ValueError('Unexpected animation frame counts')
    if [row['row'] for row in metadata['animation_rows']] != list(range(9)):
        raise ValueError('Unexpected row order')
    for row in metadata['animation_rows']:
        if len(row['durations_ms']) != row['frames'] or min(row['durations_ms']) <= 0:
            raise ValueError('Invalid frame durations')
    angles = [angle for row in metadata['look_rows'] for angle in row['angles_clockwise_from_up']]
    if angles != [index * 22.5 for index in range(16)]:
        raise ValueError('Unexpected look directions')
    if metadata['sha256'] != checksums['assets/anan.png']:
        raise ValueError('Metadata hash mismatch')
    if metadata['sprite_sheet'] != 'assets/anan.png':
        raise ValueError('Unexpected sprite sheet path')
    if metadata['required_frames'] != sum(expected_frames) + 16 + 1:
        raise ValueError('Unexpected total frame count')
    if metadata['neutral_frame'] != {'row': 0, 'column': 6, 'source_row': 0, 'source_column': 0}:
        raise ValueError('Unexpected neutral frame layout')
    manifest = json.loads((root / 'pet.json').read_text(encoding='utf-8'))
    if manifest['id'] != 'an-an-crested-gecko' or manifest['displayName'] != 'An An':
        raise ValueError('Unexpected pet identity')
    if manifest['spriteVersionNumber'] != 2 or manifest['spritesheetPath'] != metadata['sprite_sheet']:
        raise ValueError('Installation manifest does not match the sprite sheet')
    print('OK: animation metadata and file integrity')
    print('OK: local installation manifest')


if __name__ == '__main__':
    verify(Path(__file__).resolve().parents[1])
