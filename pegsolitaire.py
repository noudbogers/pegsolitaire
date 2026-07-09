```python
#!/usr/bin/env python3

"""
Peg Solitaire Solver
"""

"""
TOML Config Manager
"""
import tomllib
from pathlib import Path

class TOMLConfig:
    def __init__(self, config_file='config.toml'):
        self.config_file = Path(config_file)

#        if not self.config_file.excists():
#            raise FileNotFoundError(f"Config file not found:" {config_file}")
        
        try:
            with open(self.config_file, 'rb') as f:
                self.config = tomllib.load(f)
        except FileNotFoundError:
            print(f"Config file {config_file} not found, using defaults")
                self.config = {}
        except tomllib.TOMLDecodeError as e:
            print(f"Error parsing TOML: {e}")
            raise
    
    def get(self, key, default=None):
        """Get a top-level board configuration value"""
        return self.config.get(key, default)
    
    def get_board_config(self, board_config):
        """Get an entire board configuration"""
        if board_config not in self.config:
            raise ValueError(f"Board configuration: '{board_config}' not found")
        return self.config[board_config]

config = TOMLConfig('config.toml')

# Get top-level board configuration values
# <value variable name> = config.get('<insert value name>')

# Get entire board configurations
# <board configuration variable name> = config.get_board_config('<insert board configuration name>')

# print(f"Value: {<value variable name>}")
# print(f"Board configuration: {<board configuration variable name>}")

# Get with defaults