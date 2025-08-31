"""Data module for configuration and sample data handling."""

import json
import csv
from pathlib import Path
from typing import Dict, Any, List, Optional


# Get the data directory path
DATA_DIR = Path(__file__).parent


def load_config(config_name: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON file."""
    config_path = DATA_DIR / config_name
    
    if config_path.exists():
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                print(f"📋 Loaded config from {config_path}")
                return config
        except (json.JSONDecodeError, IOError) as e:
            print(f"⚠️  Warning: Could not load config from {config_path}: {e}")
    
    # Return default configuration
    default_config = {
        "app_name": "My Portable Package",
        "version": "1.0.0",
        "debug": True,
        "max_processing_items": 1000,
        "timeout_seconds": 30,
        "features": {
            "cross_module_support": True,
            "batch_processing": True,
            "data_validation": True
        }
    }
    
    print("📋 Using default configuration")
    return default_config


def get_sample_data(filename: str = "sample_data.csv") -> str:
    """Get sample data from CSV file."""
    data_path = DATA_DIR / filename
    
    if data_path.exists():
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"📄 Loaded sample data from {data_path}")
                return content
        except IOError as e:
            print(f"⚠️  Warning: Could not load sample data from {data_path}: {e}")
    
    # Return default sample data
    default_data = """id,name,value,category,description
1,Alpha,100,Type1,First sample item
2,Beta,250,Type2,Second sample item  
3,Gamma,175,Type1,Third sample item
4,Delta,300,Type2,Fourth sample item
5,Epsilon,125,Type3,Fifth sample item"""
    
    print("📄 Using default sample data")
    return default_data


def parse_sample_data(filename: str = "sample_data.csv") -> List[Dict[str, str]]:
    """Parse sample data into list of dictionaries."""
    data_content = get_sample_data(filename)
    
    # Parse CSV content
    lines = data_content.strip().split('\n')
    if len(lines) < 2:
        return []
    
    headers = [h.strip() for h in lines[0].split(',')]
    rows = []
    
    for line in lines[1:]:
        values = [v.strip() for v in line.split(',')]
        if len(values) == len(headers):
            row_dict = dict(zip(headers, values))
            rows.append(row_dict)
    
    print(f"📊 Parsed {len(rows)} data rows")
    return rows


def save_config(config: Dict[str, Any], config_name: str = "config.json") -> bool:
    """Save configuration to JSON file."""
    config_path = DATA_DIR / config_name
    
    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print(f"💾 Saved config to {config_path}")
        return True
    except IOError as e:
        print(f"❌ Error saving config to {config_path}: {e}")
        return False


def get_data_stats() -> Dict[str, Any]:
    """Get statistics about available data files."""
    stats = {
        "data_directory": str(DATA_DIR),
        "files": [],
        "total_files": 0,
        "config_files": 0,
        "data_files": 0
    }
    
    for file_path in DATA_DIR.iterdir():
        if file_path.is_file():
            file_info = {
                "name": file_path.name,
                "size": file_path.stat().st_size,
                "type": file_path.suffix
            }
            stats["files"].append(file_info)
            stats["total_files"] += 1
            
            if file_path.suffix == '.json':
                stats["config_files"] += 1
            elif file_path.suffix in ['.csv', '.txt', '.data']:
                stats["data_files"] += 1
    
    return stats


# Standalone testing and utilities
if __name__ == "__main__":
    print("🚀 Testing data module...")
    
    print("\n📋 Testing configuration loading:")
    config = load_config()
    print(f"Config keys: {list(config.keys())}")
    print(f"App name: {config.get('app_name')}")
    
    print("\n📄 Testing sample data:")
    sample_raw = get_sample_data()
    print(f"Sample data preview: {sample_raw[:100]}...")
    
    print("\n📊 Testing data parsing:")
    parsed_data = parse_sample_data()
    if parsed_data:
        print(f"Parsed {len(parsed_data)} rows")
        print(f"First row: {parsed_data[0]}")
    
    print("\n📈 Data statistics:")
    stats = get_data_stats()
    print(f"Data directory: {stats['data_directory']}")
    print(f"Total files: {stats['total_files']}")
    print(f"Config files: {stats['config_files']}")
    print(f"Data files: {stats['data_files']}")
    
    if stats['files']:
        print("Files found:")
        for file_info in stats['files']:
            print(f"  - {file_info['name']} ({file_info['size']} bytes)")
    
    print("✅ Data module test completed!")