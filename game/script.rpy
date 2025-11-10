# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character(_('Acheron'), color="#5015BF")
define a = Character('Phainon', color="#f5e58a")


# Le jeu commence ici
label start:

    
    show acheron_walk at left
    with dissolve
    e "Vous venez de créer un nouveau jeu Ren'Py."

    e "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"

    show phainon_splash at right
    a "fonctionne d'un enfer parfait pour ce que je veux faire"
    
    menu:

        "Oui.":
            jump choice1_yes

        "Non.":
            jump choice1_no

    label choice1_yes:

        $ menu_flag = True

        e "While creating a multi-path visual novel can be a bit more work, it can yield a unique experience."

        jump choice_done

    label choice1_no:

        $ menu_flag = False

        e "Games without menus are called kinetic novels, and there are dozens of them available to play."

        jump choice1_done

    label choice1_done:

        # ... the game continues here.

    label choice_done:
        a "ouais trust je gère comme le boss que je suis"
    return