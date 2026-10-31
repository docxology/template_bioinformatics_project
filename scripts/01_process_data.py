#!/usr/bin/env python3
"""
Example data processing script for the Bioinformatics Project Template.
This script demonstrates standard practices:
1. Loading configuration from YAML.
2. Setting up standard logging output to the `logs/` directory.
3. Checking the raw input directory and creating the processed directory.
   Processing itself is a stub (`process_data`) that logs only — no data
   files are read or written.
"""

import sys
import yaml
import logging
import argparse
from pathlib import Path


def setup_logging(config):
    """Set up logging to file and console."""
    log_file = Path(config['import_path']['logs']) / '01_process_data.log'
    log_file.parent.mkdir(parents=True, exist_ok=True)
    
    logging.basicConfig(
        level=getattr(logging, config['logging']['level']),
        format=config['logging']['format'],
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(__name__)


def load_config(config_path):
    """Load the YAML configuration file."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def process_data(config, logger):
    """Mock process function demonstrating file routing."""
    raw_dir = Path(config['import_path']['data_raw'])
    processed_dir = Path(config['import_path']['data_processed'])
    
    if not raw_dir.is_dir():
        raise FileNotFoundError(f"Raw data directory does not exist: {raw_dir}")
    processed_dir.mkdir(parents=True, exist_ok=True)
    
    logger.info(f"Raw data directory: {raw_dir}")
    logger.info(f"Filtering threshold set to: {config['processing']['filtering_threshold']}")
    logger.info(f"Targeting processed directory: {processed_dir}")
    
    logger.info("Scaffold smoke complete; no data files were read or processed.")


def main():
    parser = argparse.ArgumentParser(description="Smoke-check the bioinformatics scaffold (no data processing).")
    parser.add_argument('--config', type=str, default='config/default.yaml',
                        help='Path to the configuration file.')
    args = parser.parse_args()

    # Load configuration
    try:
        config = load_config(args.config)
    except Exception as e:
        print(f"Error loading config {args.config}: {e}", file=sys.stderr)
        sys.exit(1)

    # Setup core logger
    logger = setup_logging(config)
    logger.info("Starting data processing script.")

    try:
        process_data(config, logger)
    except Exception as e:
        logger.error(f"Fatal error during processing: {e}", exc_info=True)
        sys.exit(1)
        
    logger.info("Script execution finished successfully.")


if __name__ == '__main__':
    main()
