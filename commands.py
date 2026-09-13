#!/usr/bin/env python3
"""
Commandes personnalisées avancées pour CustomBot
Inclut: Jeux, Utilitaires, Créatifs, Recherche, Profil
"""

import random
import string
import json
from typing import List
from datetime import datetime, timedelta

# ============================
# 🎲 COMMANDES JEUX
# ============================

class GameCommands:
    """Commandes de jeux"""
    
    @staticmethod
    def cmd_ppc(args: List[str] = None) -> str:
        """Pierre-Papier-Ciseaux"""
        choices = ['pierre', 'papier', 'ciseaux']
        bot_choice = random.choice(choices)
        
        if not args:
            return "❌ Usage: /ppc <pierre|papier|ciseaux>"
        
        player_choice = args[0].lower()
        
        if player_choice not in choices:
            return f"❌ Choix invalide. Utilisez: pierre, papier ou ciseaux"
        
        # Déterminer le gagnant
        if player_choice == bot_choice:
            result = "🤝 Égalité!"
        elif (player_choice == 'pierre' and bot_choice == 'ciseaux') or \
             (player_choice == 'papier' and bot_choice == 'pierre') or \
             (player_choice == 'ciseaux' and bot_choice == 'papier'):
            result = "🎉 Vous avez gagné!"
        else:
            result = "😢 Vous avez perdu!"
        
        return f"🎮 Vous: {player_choice}\n🤖 Bot: {bot_choice}\n{result}"
    
    @staticmethod
    def cmd_dice(args: List[str] = None) -> str:
        """Lance un ou plusieurs dés"""
        if not args:
            sides = 6
            rolls = 1
        else:
            try:
                if 'd' in args[0].lower():
                    # Format: 2d6 (2 dés à 6 faces)
                    parts = args[0].lower().split('d')
                    rolls = int(parts[0]) if parts[0] else 1
                    sides = int(parts[1]) if len(parts) > 1 else 6
                else:
                    sides = int(args[0])
                    rolls = 1
            except:
                return "❌ Usage: /dice [nombre] ou /dice [rolls]d[sides] (ex: 2d6)"
        
        if rolls > 20:
            return "❌ Trop de dés à la fois (max 20)"
        if sides > 100:
            return "❌ Trop de faces (max 100)"
        
        results = [random.randint(1, sides) for _ in range(rolls)]
        total = sum(results)
        
        return f"🎲 Résultats: {results}\n📊 Total: {total}"
    
    @staticmethod
    def cmd_flip(args: List[str] = None) -> str:
        """Pile ou Face"""
        result = random.choice(['Pile', 'Face'])
        return f"🪙 Résultat: {result}"
    
    @staticmethod
    def cmd_trivia(args: List[str] = None) -> str:
        """Question trivia aléatoire"""
        trivia_questions = [
            {"q": "Quel est le plus grand océan du monde?", "a": "Pacifique"},
            {"q": "Combien de continents y a-t-il?", "a": "7"},
            {"q": "Quel est le plus haut sommet du monde?", "a": "Everest"},
            {"q": "En quelle année l'homme a-t-il marché sur la lune?", "a": "1969"},
            {"q": "Quel est le plus grand désert du monde?", "a": "Sahara"},
            {"q": "Combien de pays y a-t-il dans l'Union Européenne?", "a": "27"},
            {"q": "Quel est le plus long fleuve du monde?", "a": "Nil"},
            {"q": "Quelle est la capitale de la France?", "a": "Paris"},
        ]
        
        question = random.choice(trivia_questions)
        return f"❓ {question['q']}\n\n💡 Réponse: ||{question['a']}||"


# ============================
# 📊 COMMANDES UTILITAIRES
# ============================

class UtilityCommands:
    """Commandes utilitaires"""
    
    @staticmethod
    def cmd_convert(args: List[str] = None) -> str:
        """Convertir des unités"""
        if not args or len(args) < 3:
            return "❌ Usage: /convert <valeur> <de> <vers>\nExemples: /convert 5 km m | /convert 100 f c"
        
        try:
            value = float(args[0])
            from_unit = args[1].lower()
            to_unit = args[2].lower()
            
            # Conversions de distance
            if from_unit == 'km' and to_unit == 'm':
                result = value * 1000
            elif from_unit == 'm' and to_unit == 'km':
                result = value / 1000
            elif from_unit == 'miles' and to_unit == 'km':
                result = value * 1.60934
            elif from_unit == 'km' and to_unit == 'miles':
                result = value / 1.60934
            
            # Conversions de température
            elif from_unit == 'c' and to_unit == 'f':
                result = (value * 9/5) + 32
            elif from_unit == 'f' and to_unit == 'c':
                result = (value - 32) * 5/9
            
            # Conversions de poids
            elif from_unit == 'kg' and to_unit == 'lb':
                result = value * 2.20462
            elif from_unit == 'lb' and to_unit == 'kg':
                result = value / 2.20462
            
            else:
                return f"❌ Conversion '{from_unit}' → '{to_unit}' non supportée"
            
            return f"🔄 {value} {from_unit} = {result:.2f} {to_unit}"
        
        except ValueError:
            return "❌ La valeur doit être un nombre"
    
    @staticmethod
    def cmd_password(args: List[str] = None) -> str:
        """Génère un mot de passe aléatoire"""
        length = 12
        if args:
            try:
                length = int(args[0])
                if length < 4 or length > 64:
                    return "❌ La longueur doit être entre 4 et 64"
            except:
                pass
        
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(characters) for _ in range(length))
        
        return f"🔐 Mot de passe généré ({length} caractères):\n```{password}```"
    
    @staticmethod
    def cmd_calc(args: List[str] = None) -> str:
        """Calculatrice"""
        if not args or len(args) < 3:
            return "❌ Usage: /calc <nombre1> <opérateur> <nombre2>\nOpérateurs: +, -, *, /, %, ^"
        
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
            elif op == '%':
                result = num1 % num2
            elif op == '^':
                result = num1 ** num2
            else:
                return f"❌ Opérateur '{op}' non reconnu"
            
            return f"🧮 {num1} {op} {num2} = {result}"
        
        except ValueError:
            return "❌ Veuillez entrer des nombres valides"
    
    @staticmethod
    def cmd_qrcode(args: List[str] = None) -> str:
        """Génère un code QR (simulation)"""
        if not args:
            return "❌ Usage: /qrcode <texte>"
        
        text = " ".join(args)
        # Simulation - dans une vraie app, on générerait un QR code
        return f"📱 QR Code pour: {text}\n(Intégration QR code requise)"


# ============================
# 🎨 COMMANDES CRÉATIFS
# ============================

class CreativeCommands:
    """Commandes créatives"""
    
    @staticmethod
    def cmd_quote(args: List[str] = None) -> str:
        """Citation aléatoire inspirante"""
        quotes = [
            ("Le succès est la somme de petits efforts répétés jour après jour.", "Robert Collier"),
            ("L'avenir appartient à ceux qui croient en la beauté de leurs rêves.", "Eleanor Roosevelt"),
            ("La vie est 10% ce qui vous arrive et 90% comment vous réagissez.", "Charles R. Swindoll"),
            ("Le meilleur moment pour planter un arbre était il y a 20 ans. Le deuxième meilleur moment est maintenant.", "Proverbe chinois"),
            ("Vous êtes le seul maître de votre destin.", "Barack Obama"),
            ("La perfection n'existe pas, mais si tu poursuis la perfection, tu peux attraper l'excellence.", "Vince Lombardi"),
        ]
        
        quote, author = random.choice(quotes)
        return f'💡 "{quote}"\n— {author}'
    
    @staticmethod
    def cmd_joke(args: List[str] = None) -> str:
        """Blague aléatoire"""
        jokes = [
            "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant? Parce que sinon ils tombent dans le bateau!",
            "Qu'est-ce qu'un crocodile qui surveille la pharmacie? Un Lacoste-garde!",
            "Quel est le comble pour un électricien? De ne pas être au courant!",
            "Comment appelle-t-on un chat tombé dans un pot de peinture le jour de Noël? Un chat-peint de Noël!",
            "Qu'est-ce qu'un canif? Un petit fien!",
        ]
        
        return f"😂 {random.choice(jokes)}"
    
    @staticmethod
    def cmd_ascii(args: List[str] = None) -> str:
        """Art ASCII aléatoire"""
        ascii_arts = [
            """
    \\___/
    (o o)
    ( = )
    (   )
    ( | )
   /|   |\\
    |   |
   /     \\
  (       )
            """,
            """
      ^
     / \\
    /   \\
   /  U  \\
  /_______\\
   |     |
   |     |
   |     |
   |_____|
            """,
            """
   /\\_/\\
  ( o.o )
   > ^ <
  /|   |\\
   |   |
  _|   |_
            """
        ]
        
        return f"🎨 Art ASCII:\n```{random.choice(ascii_arts)}```"
    
    @staticmethod
    def cmd_story(args: List[str] = None) -> str:
        """Génère une micro-histoire"""
        characters = ["Un chevalier", "Une sorcière", "Un pirate", "Un robot", "Un alien"]
        places = ["au château", "dans la forêt", "sur une île", "en montagne", "dans l'espace"]
        actions = ["a trouvé un trésor", "a sauvé quelqu'un", "a découvert un secret", "a fait une amitié", "a changé le monde"]
        
        char = random.choice(characters)
        place = random.choice(places)
        action = random.choice(actions)
        
        return f"📖 Histoire:\n{char} {place} {action}. C'était l'aventure de sa vie! ✨"


# ============================
# 👤 COMMANDES PROFIL
# ============================

class ProfileCommands:
    """Commandes de profil utilisateur"""
    
    def __init__(self):
        self.users = {}
    
    def cmd_profile(self, user: str = "Anonyme", args: List[str] = None) -> str:
        """Affiche le profil de l'utilisateur"""
        if user not in self.users:
            self.users[user] = {
                'created': datetime.now().isoformat(),
                'messages': 0,
                'level': 1,
                'xp': 0,
                'achievements': []
            }
        
        profile = self.users[user]
        level = profile['level']
        xp = profile['xp']
        
        return f"""
👤 Profil de {user}
━━━━━━━━━━━━━━━━━━━━━━
⭐ Niveau: {level}
📊 XP: {xp}/1000
💬 Messages: {profile['messages']}
🏆 Réalisations: {len(profile['achievements'])}
📅 Membre depuis: {profile['created'][:10]}
        """
    
    def cmd_stats(self, user: str = "Anonyme", args: List[str] = None) -> str:
        """Affiche les statistiques"""
        if user not in self.users:
            return "❌ Aucune statistique disponible"
        
        profile = self.users[user]
        return f"""
📊 Statistiques de {user}
━━━━━━━━━━━━━━━━━━━━━━
💬 Messages: {profile['messages']}
⭐ Niveau: {profile['level']}
📈 XP: {profile['xp']}
🏆 Réalisations: {profile['achievements']}
        """
    
    def cmd_achievements(self, user: str = "Anonyme", args: List[str] = None) -> str:
        """Affiche les réalisations"""
        achievements_list = [
            "🎖️ Premier message",
            "⭐ 100 messages",
            "🚀 Niveau 5",
            "👑 Admin",
            "🎯 1000 XP",
        ]
        
        return f"""
🏆 Réalisations disponibles
━━━━━━━━━━━━━━━━━━━━━━
{chr(10).join(achievements_list)}
        """


# ============================
# 🔍 COMMANDES RECHERCHE/INFO
# ============================

class SearchCommands:
    """Commandes de recherche et d'informations"""
    
    @staticmethod
    def cmd_info(args: List[str] = None) -> str:
        """Informations générales"""
        info = {
            'python': 'Langage de programmation puissant et polyvalent',
            'github': 'Plateforme de partage et collaboration de code',
            'bot': 'Programme automatisé qui exécute des tâches',
            'ai': 'Intelligence Artificielle - simulation de l\'intelligence humaine',
        }
        
        if not args:
            return "❌ Usage: /info <sujet>\nSujets disponibles: " + ", ".join(info.keys())
        
        topic = args[0].lower()
        if topic in info:
            return f"ℹ️ {topic.upper()}\n{info[topic]}"
        else:
            return f"❌ Sujet '{topic}' non trouvé"
    
    @staticmethod
    def cmd_weather(args: List[str] = None) -> str:
        """Simule une météo (nécessite API réelle pour être fonctionnel)"""
        if not args:
            return "❌ Usage: /weather <ville>"
        
        city = " ".join(args)
        temps = random.choice(['Ensoleillé ☀️', 'Nuageux ☁️', 'Pluie 🌧️', 'Neige ❄️', 'Orageux ⛈️'])
        temp = random.randint(-5, 35)
        humidity = random.randint(30, 90)
        
        return f"""
🌍 Météo à {city}
━━━━━━━━━━━━━━━━━━━━━━
Condition: {temps}
Température: {temp}°C
Humidité: {humidity}%
        """
    
    @staticmethod
    def cmd_time(args: List[str] = None) -> str:
        """Affiche l'heure et la date"""
        now = datetime.now()
        return f"""
⏰ Date et Heure
━━━━━━━━━━━━━━━━━━━━━━
🕐 Heure: {now.strftime('%H:%M:%S')}
📅 Date: {now.strftime('%d/%m/%Y')}
📆 Jour: {['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'][now.weekday()]}
        """


# ============================
# 🎯 FONCTION D'ENREGISTREMENT
# ============================

def register_custom_commands(bot):
    """Enregistre toutes les commandes personnalisées"""
    
    # Commandes Jeux
    bot.register_command('ppc', 'Pierre-Papier-Ciseaux', GameCommands.cmd_ppc)
    bot.register_command('dice', 'Lance les dés', GameCommands.cmd_dice)
    bot.register_command('flip', 'Pile ou Face', GameCommands.cmd_flip)
    bot.register_command('trivia', 'Question trivia', GameCommands.cmd_trivia)
    
    # Commandes Utilitaires
    bot.register_command('convert', 'Convertir des unités', UtilityCommands.cmd_convert)
    bot.register_command('password', 'Générer un mot de passe', UtilityCommands.cmd_password)
    bot.register_command('calc', 'Calculatrice', UtilityCommands.cmd_calc)
    bot.register_command('qrcode', 'Générer un QR code', UtilityCommands.cmd_qrcode)
    
    # Commandes Créatifs
    bot.register_command('quote', 'Citation inspirante', CreativeCommands.cmd_quote)
    bot.register_command('joke', 'Blague aléatoire', CreativeCommands.cmd_joke)
    bot.register_command('ascii', 'Art ASCII', CreativeCommands.cmd_ascii)
    bot.register_command('story', 'Micro-histoire', CreativeCommands.cmd_story)
    
    # Commandes Profil
    profile_cmd = ProfileCommands()
    bot.register_command('profile', 'Voir votre profil', lambda args: profile_cmd.cmd_profile("Utilisateur", args))
    bot.register_command('stats', 'Voir statistiques', lambda args: profile_cmd.cmd_stats("Utilisateur", args))
    bot.register_command('achievements', 'Réalisations', lambda args: profile_cmd.cmd_achievements("Utilisateur", args))
    
    # Commandes Recherche
    bot.register_command('info', 'Informations sur un sujet', SearchCommands.cmd_info)
    bot.register_command('weather', 'Météo', SearchCommands.cmd_weather)
    bot.register_command('time', 'Heure et date', SearchCommands.cmd_time)
