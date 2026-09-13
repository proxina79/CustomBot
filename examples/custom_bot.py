#!/usr/bin/env python3
"""
Exemple: Bot personnalisé avec commandes additionnelles
"""

import sys
sys.path.insert(0, '..')

from main import CustomBot
from typing import List

# Créer une instance du bot
bot = CustomBot("MyCoolBot")

# Ajouter des commandes personnalisées

def cmd_calc(args: List[str]) -> str:
    """Effectue un calcul simple"""
    if not args or len(args) < 3:
        return "❌ Usage: /calc <nombre1> <operateur> <nombre2>"
    
    try:
        num1 = float(args[0])
        op = args[1]
        num2 = float(args[2])
        
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                return "❌ Division par zéro impossible"
            result = num1 / num2
        else:
            return f"❌ Opérateur '{op}' non reconnu. Utilisez +, -, *, /"
        
        return f"🧮 {num1} {op} {num2} = {result}"
    except ValueError:
        return "❌ Veuillez entrer des nombres valides"

def cmd_joke(args: List[str]) -> str:
    """Raconte une blague"""
    jokes = [
        "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant? Parce que sinon ils tombent dans le bateau!",
        "Qu'est-ce qu'un crocodile qui surveille la pharmacie? Un Lacoste-garde!",
        "Quel est le comble pour un électricien? De ne pas être au courant!",
    ]
    import random
    return f"😂 {random.choice(jokes)}"

def cmd_dice(args: List[str]) -> str:
    """Lance un dé"""
    import random
    sides = 6
    if args:
        try:
            sides = int(args[0])
        except:
            pass
    result = random.randint(1, sides)
    return f"🎲 Résultat: {result}/{sides}"

# Enregistrer les commandes personnalisées
bot.register_command('calc', 'Effectue un calcul (ex: /calc 5 + 3)', cmd_calc)
bot.register_command('joke', 'Raconte une blague', cmd_joke)
bot.register_command('dice', 'Lance un dé', cmd_dice)

if __name__ == "__main__":
    bot.start()
