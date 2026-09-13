# 🤖 CustomBot - Bot Personnalisé

Un bot flexible avec système de commandes personnalisables que vous pouvez adapter à n'importe quelle plateforme.

## 🌟 Caractéristiques

- ✅ **Système de commandes flexible** - Ajoutez vos propres commandes facilement
- ✅ **Architecture modulaire** - Facile à étendre et modifier
- ✅ **Commandes intégrées** - `/aide`, `/bonjour`, `/heure`, `/statut`, `/echo`
- ✅ **Gestion d'erreurs** - Traitement sécurisé des erreurs
- ✅ **Interface simple** - Facile à utiliser et comprendre

## 📋 Commandes disponibles

| Commande | Description | Usage |
|----------|-------------|-------|
| `/aide` | Affiche toutes les commandes | `/aide` |
| `/bonjour` | Salue l'utilisateur | `/bonjour [nom]` |
| `/heure` | Affiche l'heure actuelle | `/heure` |
| `/statut` | Affiche le statut du bot | `/statut` |
| `/echo` | Répète votre message | `/echo [message]` |

## 🚀 Installation

### Prérequis
- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes

1. **Cloner le repository**
```bash
git clone https://github.com/proxina79/CustomBot.git
cd CustomBot
```

2. **Créer un environnement virtuel (optionnel mais recommandé)**
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

## 💻 Utilisation

### Démarrer le bot
```bash
python main.py
```

### Utiliser le bot
```
🤖 CustomBot démarré!
==================================================
Tapez '/aide' pour voir les commandes
Tapez 'quit' pour quitter

Vous: /aide
CustomBot: 
==================================================
📋 AIDE - Commandes disponibles (CustomBot)
==================================================

  /aide
    → Affiche la liste de toutes les commandes

  /bonjour
    → Salue l'utilisateur
...
```

## 🔧 Ajouter une commande personnalisée

### Méthode 1 : Via le code

Modifiez `main.py` et ajoutez votre fonction :

```python
def cmd_ma_commande(self, args: List[str] = None) -> str:
    """Commande: ma_commande"""
    return "Réponse de ma commande"

# Dans load_commands()
self.register_command(
    'ma_commande',
    'Description de ma commande',
    self.cmd_ma_commande
)
```

### Méthode 2 : Via un plugin

Utilisez `plugins.py` pour charger les commandes dynamiquement :

```python
from main import CustomBot

bot = CustomBot()
bot.register_command('custom', 'Ma commande', lambda args: "Coucou!")
```

## 📁 Structure du projet

```
CustomBot/
├── main.py              # Fichier principal du bot
├── plugins.py           # Système de plugins
├── requirements.txt     # Dépendances Python
├── config.json          # Configuration
├── README.md            # Ce fichier
└── examples/            # Exemples d'utilisation
    └── custom_bot.py    # Exemple de bot personnalisé
```

## 🎯 Cas d'usage

- 🎮 Bot Discord avec commandes personnalisées
- 💬 Bot Telegram pour groupes
- 📱 Bot WhatsApp (non officiel)
- 🤖 Bot personnalisé sur votre serveur
- 🔌 Intégration dans d'autres applications

## 🛠️ Configuration

Modifiez `config.json` pour personnaliser :

```json
{
  "bot_name": "CustomBot",
  "prefix": "/",
  "debug": true,
  "log_messages": true
}
```

## 🤝 Contribution

Les contributions sont bienvenues ! N'hésitez pas à :
- Proposer des améliorations
- Signaler des bugs
- Ajouter de nouvelles commandes
- Améliorer la documentation

## 📝 Licence

Ce projet est sous licence MIT. Voir `LICENSE` pour plus de détails.

## 📞 Support

Pour toute question ou problème, ouvrez une issue sur GitHub.

---

**Développé avec ❤️ par proxina79**
