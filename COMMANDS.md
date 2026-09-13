# Commandes Personnalisées Avancées - Documentation Complète

## 📋 Index des Commandes

### 🎲 JEUX (4 commandes)
- [Pierre-Papier-Ciseaux](#ppc)
- [Lancer les dés](#dice)
- [Pile ou Face](#flip)
- [Trivia](#trivia)

### 📊 UTILITAIRES (4 commandes)
- [Convertir des unités](#convert)
- [Générateur de mot de passe](#password)
- [Calculatrice](#calc)
- [QR Code](#qrcode)

### 🎨 CRÉATIFS (4 commandes)
- [Citations inspirantes](#quote)
- [Blagues](#joke)
- [Art ASCII](#ascii)
- [Micro-histoires](#story)

### 👤 PROFIL (3 commandes)
- [Profil utilisateur](#profile)
- [Statistiques](#stats)
- [Réalisations](#achievements)

### 🔍 RECHERCHE/INFO (3 commandes)
- [Informations](#info)
- [Météo](#weather)
- [Heure et Date](#time)

---

## 🎲 COMMANDES JEUX

### /ppc
**Pierre-Papier-Ciseaux contre le bot**

**Syntaxe:**
```
/ppc <pierre|papier|ciseaux>
```

**Exemples:**
```
/ppc pierre
/ppc papier
/ppc ciseaux
```

**Résultat:**
```
🎮 Vous: pierre
🤖 Bot: ciseaux
🎉 Vous avez gagné!
```

---

### /dice
**Lance un ou plusieurs dés**

**Syntaxe:**
```
/dice [sides]           # Lance 1 dé
/dice [rolls]d[sides]   # Lance plusieurs dés
```

**Exemples:**
```
/dice              # Lance un d6 (par défaut)
/dice 20           # Lance un d20
/dice 2d6          # Lance 2 dés à 6 faces
/dice 3d10         # Lance 3 dés à 10 faces
```

**Résultat:**
```
🎲 Résultats: [4, 5, 3]
📊 Total: 12
```

---

### /flip
**Pile ou Face**

**Syntaxe:**
```
/flip
```

**Résultat:**
```
🪙 Résultat: Face
```

---

### /trivia
**Question trivia aléatoire**

**Syntaxe:**
```
/trivia
```

**Résultat:**
```
❓ Quel est le plus grand océan du monde?

💡 Réponse: ||Pacifique||
```

---

## 📊 COMMANDES UTILITAIRES

### /convert
**Convertit des unités (distance, température, poids)**

**Syntaxe:**
```
/convert <valeur> <de> <vers>
```

**Unités supportées:**
- Distance: `km`, `m`, `miles`
- Température: `c` (Celsius), `f` (Fahrenheit)
- Poids: `kg`, `lb`

**Exemples:**
```
/convert 5 km m          # km vers mètres
/convert 100 f c         # Fahrenheit vers Celsius
/convert 70 kg lb        # kg vers livres
/convert 5 miles km      # miles vers km
```

**Résultat:**
```
🔄 5 km = 5000.00 m
🔄 100 f = 37.78 c
🔄 70 kg = 154.32 lb
```

---

### /password
**Génère un mot de passe aléatoire sécurisé**

**Syntaxe:**
```
/password [longueur]    # Longueur 4-64 (défaut: 12)
```

**Exemples:**
```
/password           # Mot de passe de 12 caractères
/password 20        # Mot de passe de 20 caractères
/password 8         # Mot de passe de 8 caractères
```

**Résultat:**
```
🔐 Mot de passe généré (12 caractères):
```
Ab3$xYz@Km9!
```
```

---

### /calc
**Calculatrice simple**

**Syntaxe:**
```
/calc <nombre1> <opérateur> <nombre2>
```

**Opérateurs supportés:**
- `+` Addition
- `-` Soustraction
- `*` Multiplication
- `/` Division
- `%` Modulo (reste)
- `^` Puissance

**Exemples:**
```
/calc 10 + 5
/calc 20 - 3
/calc 7 * 8
/calc 100 / 4
/calc 17 % 5
/calc 2 ^ 8
```

**Résultat:**
```
🧮 10 + 5 = 15
🧮 2 ^ 8 = 256
```

---

### /qrcode
**Génère un QR code**

**Syntaxe:**
```
/qrcode <texte>
```

**Exemples:**
```
/qrcode https://github.com
/qrcode Mon message secret
```

---

## 🎨 COMMANDES CRÉATIFS

### /quote
**Affiche une citation inspirante aléatoire**

**Syntaxe:**
```
/quote
```

**Résultat:**
```
💡 "Le succès est la somme de petits efforts répétés jour après jour."
— Robert Collier
```

---

### /joke
**Raconte une blague aléatoire**

**Syntaxe:**
```
/joke
```

**Résultat:**
```
😂 Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant?
    Parce que sinon ils tombent dans le bateau!
```

---

### /ascii
**Affiche un art ASCII aléatoire**

**Syntaxe:**
```
/ascii
```

**Résultat:**
```
🎨 Art ASCII:
   /\_/\
  ( o.o )
   > ^ <
  /|   |\
```

---

### /story
**Génère une micro-histoire aléatoire**

**Syntaxe:**
```
/story
```

**Résultat:**
```
📖 Histoire:
Un chevalier au château a trouvé un trésor.
C'était l'aventure de sa vie! ✨
```

---

## 👤 COMMANDES PROFIL

### /profile
**Affiche votre profil utilisateur**

**Syntaxe:**
```
/profile
```

**Résultat:**
```
👤 Profil de Utilisateur
━━━━━━━━━━━━━━━━━━━━━━
⭐ Niveau: 1
📊 XP: 0/1000
💬 Messages: 0
🏆 Réalisations: 0
📅 Membre depuis: 2026-09-13
```

---

### /stats
**Affiche vos statistiques détaillées**

**Syntaxe:**
```
/stats
```

**Résultat:**
```
📊 Statistiques de Utilisateur
━━━━━━━━━━━━━━━━━━━━━━
💬 Messages: 42
⭐ Niveau: 3
📈 XP: 250
🏆 Réalisations: ['Premier message', 'Niveau 2']
```

---

### /achievements
**Liste toutes les réalisations disponibles**

**Syntaxe:**
```
/achievements
```

**Résultat:**
```
🏆 Réalisations disponibles
━━━━━━━━━━━━━━━━━━━━━━
🎖️ Premier message
⭐ 100 messages
🚀 Niveau 5
👑 Admin
🎯 1000 XP
```

---

## 🔍 COMMANDES RECHERCHE/INFO

### /info
**Donne des informations sur un sujet**

**Syntaxe:**
```
/info <sujet>
```

**Sujets disponibles:**
- `python` - Langage de programmation
- `github` - Plateforme de code
- `bot` - Programme automatisé
- `ai` - Intelligence Artificielle

**Exemples:**
```
/info python
/info github
/info bot
/info ai
```

**Résultat:**
```
ℹ️ PYTHON
Langage de programmation puissant et polyvalent
```

---

### /weather
**Affiche la météo (simulation)**

**Syntaxe:**
```
/weather <ville>
```

**Exemples:**
```
/weather Paris
/weather New York
/weather Tokyo
```

**Résultat:**
```
🌍 Météo à Paris
━━━━━━━━━━━━━━━━━━━━━━
Condition: Ensoleillé ☀️
Température: 22°C
Humidité: 65%
```

---

### /time
**Affiche l'heure et la date actuelle**

**Syntaxe:**
```
/time
```

**Résultat:**
```
⏰ Date et Heure
━━━━━━━━━━━━━━━━━━━━━━
🕐 Heure: 14:30:45
📅 Date: 13/09/2026
📆 Jour: Samedi
```

---

## 🚀 Utilisation Rapide

### Démarrer le bot avancé

```bash
python bot_advanced.py
```

### Exemples de session

```
🤖 CustomBot Pro démarré!
==================================================
Tapez '/aide' pour voir les commandes
Tapez 'quit' pour quitter

Vous: /aide

Vous: /ppc pierre
CustomBot Pro: 🎮 Vous: pierre
🤖 Bot: papier
😢 Vous avez perdu!

Vous: /calc 5 * 3
CustomBot Pro: 🧮 5 * 3 = 15

Vous: /quote
CustomBot Pro: 💡 "Le succès est..."

Vous: /weather Paris
CustomBot Pro: 🌍 Météo à Paris...

Vous: quit
```

---

## 💡 Conseils

1. **Combinaisons utiles:**
   - Utilisez `/calc` pour vos calculs rapides
   - Utilisez `/convert` pour les conversions d'unités
   - Utilisez `/password` pour générer des mots de passe sécurisés

2. **Pour les jeux:**
   - `/ppc` pour se détendre
   - `/trivia` pour apprendre des faits
   - `/dice` pour les jeux de rôle

3. **Pour l'inspiration:**
   - `/quote` pour de la motivation
   - `/joke` pour rire
   - `/story` pour l'imagination

---

## 📝 Notes

- Les commandes sont **case-insensitive** (majuscules/minuscules ne comptent pas)
- Utilisez `/aide` pour voir la liste complète
- Toutes les commandes sont **gratuites** et **sans limite**
- Les données sont stockées **localement**

---

**Bon amusement avec CustomBot Pro! 🎉**
