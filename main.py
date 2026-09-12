#!/usr/bin/env python3
"""
CustomBot - Bot personnalisé avec système de commandes flexible
"""

import json
import os
from typing import Dict, Callable, List
from datetime import datetime

class CustomBot:
    def __init__(self, bot_name: str = "CustomBot"):
        self.bot_name = bot_name
        self.commands: Dict[str, Callable] = {}
        self.prefix = "/"
        self.running = False
        self.load_commands()
        
    def register_command(self, name: str, description: str, callback: Callable):
        """Enregistre une nouvelle commande"""
        self.commands[name] = {
            'callback': callback,
            'description': description
        }
        print(f"✓ Commande '{name}' enregistrée")
    
    def load_commands(self):
        """Charge les commandes par défaut"""
        self.register_command(
            'aide',
            'Affiche la liste de toutes les commandes',
            self.cmd_aide
        )
        self.register_command(
            'bonjour',
            'Salue l\'utilisateur',
            self.cmd_bonjour
        )
        self.register_command(
            'heure',
            'Affiche l\'heure actuelle',
            self.cmd_heure
        )
        self.register_command(
            'statut',
            'Affiche le statut du bot',
            self.cmd_statut
        )
        self.register_command(
            'echo',
            'Répète le message reçu',
            self.cmd_echo
        )
    
    def cmd_aide(self, args: List[str] = None) -> str:
        """Commande: aide"""
        response = f"\n{'='*50}\n"
        response += f"📋 AIDE - Commandes disponibles ({self.bot_name})\n"
        response += f"{'='*50}\n\n"
        
        for cmd_name, cmd_info in self.commands.items():
            response += f"  {self.prefix}{cmd_name}\n"
            response += f"    → {cmd_info['description']}\n\n"
        
        response += f"{'='*50}\n"
        return response
    
    def cmd_bonjour(self, args: List[str] = None) -> str:
        """Commande: bonjour"""
        user = args[0] if args else "utilisateur"
        return f"👋 Bonjour {user}! Bienvenue sur {self.bot_name}"
    
    def cmd_heure(self, args: List[str] = None) -> str:
        """Commande: heure"""
        now = datetime.now().strftime("%H:%M:%S")
        return f"⏰ Heure actuelle: {now}"
    
    def cmd_statut(self, args: List[str] = None) -> str:
        """Commande: statut"""
        return f"✅ {self.bot_name} est en ligne et fonctionne normalement"
    
    def cmd_echo(self, args: List[str] = None) -> str:
        """Commande: echo"""
        if not args:
            return "❌ Usage: /echo <message>"
        message = " ".join(args)
        return f"🔊 Écho: {message}"
    
    def process_message(self, message: str, user: str = "Anonyme") -> str:
        """Traite un message reçu"""
        message = message.strip()
        
        # Vérifier si c'est une commande
        if not message.startswith(self.prefix):
            return f"ℹ️ Pour utiliser une commande, commencez par '{self.prefix}'. Tapez '{self.prefix}aide' pour voir la liste."
        
        # Extraire la commande et les arguments
        parts = message[len(self.prefix):].split()
        command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        # Exécuter la commande
        if command in self.commands:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] {user} → /{command} {' '.join(args)}")
            try:
                response = self.commands[command]['callback'](args)
                return response
            except Exception as e:
                return f"❌ Erreur lors de l'exécution: {str(e)}"
        else:
            return f"❌ Commande '{command}' non trouvée. Tapez '{self.prefix}aide' pour la liste des commandes."
    
    def start(self):
        """Démarre le bot en mode interactif"""
        self.running = True
        print(f"\n{'='*50}")
        print(f"🤖 {self.bot_name} démarré!")
        print(f"{'='*50}")
        print(f"Tapez '{self.prefix}aide' pour voir les commandes")
        print("Tapez 'quit' pour quitter\n")
        
        while self.running:
            try:
                user_input = input(f"Vous: ").strip()
                
                if user_input.lower() == 'quit':
                    self.stop()
                    break
                
                if not user_input:
                    continue
                
                response = self.process_message(user_input, "Utilisateur")
                print(f"{self.bot_name}: {response}\n")
                
            except KeyboardInterrupt:
                print("\n")
                self.stop()
                break
            except Exception as e:
                print(f"❌ Erreur: {str(e)}\n")
    
    def stop(self):
        """Arrête le bot"""
        self.running = False
        print(f"\n{'='*50}")
        print(f"👋 {self.bot_name} arrêté. Au revoir!")
        print(f"{'='*50}\n")


if __name__ == "__main__":
    # Créer et démarrer le bot
    bot = CustomBot("CustomBot")
    bot.start()
