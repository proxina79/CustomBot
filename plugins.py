#!/usr/bin/env python3
"""
Système de plugins pour CustomBot
Permet de charger des commandes dynamiquement
"""

import os
import sys
import importlib.util
from typing import Dict, Callable, List
from pathlib import Path

class PluginManager:
    def __init__(self, bot):
        self.bot = bot
        self.plugins: Dict[str, any] = {}
        self.plugins_dir = Path("plugins")
    
    def load_plugins(self):
        """Charge tous les plugins du dossier 'plugins'"""
        if not self.plugins_dir.exists():
            print(f"⚠️  Dossier {self.plugins_dir} non trouvé")
            return
        
        plugin_files = list(self.plugins_dir.glob("*.py"))
        
        for plugin_file in plugin_files:
            if plugin_file.name.startswith("_"):
                continue
            
            try:
                self.load_plugin(plugin_file)
            except Exception as e:
                print(f"❌ Erreur lors du chargement de {plugin_file}: {e}")
    
    def load_plugin(self, plugin_path):
        """Charge un plugin spécifique"""
        spec = importlib.util.spec_from_file_location(
            plugin_path.stem,
            plugin_path
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Chercher les commandes dans le module
        if hasattr(module, 'register_commands'):
            module.register_commands(self.bot)
            print(f"✓ Plugin '{plugin_path.stem}' chargé")
        
        self.plugins[plugin_path.stem] = module
    
    def unload_plugin(self, name: str):
        """Décharge un plugin"""
        if name in self.plugins:
            del self.plugins[name]
            print(f"✓ Plugin '{name}' déchargé")
        else:
            print(f"❌ Plugin '{name}' non trouvé")


def create_simple_plugin(command_name: str, command_func: Callable, description: str):
    """
    Crée un plugin simple
    
    Exemple:
    plugin = create_simple_plugin(
        'ping',
        lambda args: 'Pong!',
        'Commande ping'
    )
    """
    return {
        'name': command_name,
        'func': command_func,
        'description': description
    }
