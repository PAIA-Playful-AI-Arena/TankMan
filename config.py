from .src.TankMan import TankMan
import pygame
from os import path
from mlgame.utils.parse_config import read_json_file, parse_config
from argparse import ArgumentTypeError

GAME_SETUP = {
    "game": TankMan,

    "ml_clients":TankMan.ai_clients(),
    "dynamic_ml_clients":True
}

config_file = path.join(path.dirname(__file__), "game_config.json")

config_data = read_json_file(config_file)
GAME_VERSION = config_data["version"]
GAME_PARAMS = parse_config(config_data)

