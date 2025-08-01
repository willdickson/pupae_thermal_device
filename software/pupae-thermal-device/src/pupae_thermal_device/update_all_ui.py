import pathlib
import subprocess

print()
print('updating .ui files')

cwd = pathlib.Path().cwd()

for item in pathlib.Path(cwd, 'ui').iterdir():
    if item.suffix == '.ui':
        input_name = str(item)
        output_name = f'ui_{item.stem}.py'
        cmd_list = ['uv', 'run', 'pyside6-uic', input_name, '-o', output_name]
        cmd_str = ' '.join(cmd_list)
        print(f'  {cmd_str}')
        subprocess.run(['uv', 'run', 'pyside6-uic', item, '-o', output_name])
print('done')

