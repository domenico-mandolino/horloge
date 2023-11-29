from datetime import datetime

# Obtenir la date et l'heure actuelles
heure_actuelle = datetime.now().time()

# Formater la date et l'heure selon le format souhaité
format_heure = heure_actuelle.strftime("%H:%M:%S")

# Afficher la date et l'heure dans le format spécifié
print("Date et heure au format demandé :", format_heure)
