#!/usr/bin/env python3
"""
Bot avancé avec toutes les commandes personnalisées
Intègre: Jeux, Utilitaires, Créatifs, Profil, Recherche
"""

import sys
sys.path.insert(0, '.')

from main import CustomBot
from commands import register_custom_commands

def main():
    # Créer le bot
    bot = CustomBot("CustomBot Pro")
    
    # Enregistrer toutes les commandes avancées
    print("\n🔧 Chargement des commandes avancées...\n")
    register_custom_commands(bot)
    
    # Démarrer le bot
    bot.start()

if __name__ == "__main__":
    main()
