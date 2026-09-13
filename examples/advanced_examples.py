#!/usr/bin/env python3
"""
Exemples d'utilisation avancée du bot
"""

import sys
sys.path.insert(0, '..')

from main import CustomBot
from commands import (
    GameCommands,
    UtilityCommands,
    CreativeCommands,
    SearchCommands,
    ProfileCommands,
    register_custom_commands
)

def example_games():
    """Exemples des commandes de jeux"""
    print("\n=== JEUX ===")
    print(GameCommands.cmd_ppc(['papier']))
    print(GameCommands.cmd_dice(['2d6']))
    print(GameCommands.cmd_flip())
    print(GameCommands.cmd_trivia())

def example_utilities():
    """Exemples des commandes utilitaires"""
    print("\n=== UTILITAIRES ===")
    print(UtilityCommands.cmd_convert(['5', 'km', 'm']))
    print(UtilityCommands.cmd_password(['16']))
    print(UtilityCommands.cmd_calc(['10', '+', '5']))

def example_creative():
    """Exemples des commandes créatives"""
    print("\n=== CRÉATIFS ===")
    print(CreativeCommands.cmd_quote())
    print(CreativeCommands.cmd_joke())
    print(CreativeCommands.cmd_story())

def example_search():
    """Exemples des commandes de recherche"""
    print("\n=== RECHERCHE ===")
    print(SearchCommands.cmd_info(['python']))
    print(SearchCommands.cmd_weather(['Paris']))
    print(SearchCommands.cmd_time())

def example_full_bot():
    """Exemple du bot complet"""
    print("\n=== BOT COMPLET ===")
    bot = CustomBot("Demo Bot")
    register_custom_commands(bot)
    
    # Simuler quelques commandes
    messages = [
        '/aide',
        '/ppc pierre',
        '/calc 15 * 3',
        '/quote',
    ]
    
    for msg in messages:
        response = bot.process_message(msg, "Demo User")
        print(f"Commande: {msg}")
        print(f"Réponse: {response}")
        print()

if __name__ == "__main__":
    print("\n" + "="*60)
    print("EXEMPLES D'UTILISATION - CUSTOMBOT")
    print("="*60)
    
    # Lancer les exemples
    example_games()
    example_utilities()
    example_creative()
    example_search()
    example_full_bot()
    
    print("\n" + "="*60)
    print("Exemples terminés!")
    print("Pour démarrer le bot interactif: python bot_advanced.py")
    print("="*60 + "\n")
