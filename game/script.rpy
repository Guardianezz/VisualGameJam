# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define a = Character('Agnes',color="#123e5f")
define m = Character('Mallaury',color="#149a5e")
define g = Character('Gustave', color="#b01394")
define b = Character('Baron Vureloi',color="#4a6c8d")

$ default = mallaury_eat_apple

transform upCharacter:
    #monte le perso
    yoffset -300
    linear 0.1
    #le descend
    yoffset 0
    linear 0.1

# Le jeu commence ici
label start:

    scene bc_fond
    show mallaury at right
    with dissolve

    m "Alors Gustave qu'allez-vous faire de beau aujourd'hui ?"
    g "Je vais m'occuper de nettoyer le domaine et vous que comptez vous faire ?"

    m "Je ne sais pas encore avez vous des suggestions mon cher ?"
    g "Je vous conseille de profitez que le soleil soit à son zénith pour faire un tour au marché, l'air frais vous feras le plus grand bien."
    m "Un grand merci mon très cher Gustave je vais suivre votre conseil ! En route pour le marché !"
    
    hide mallaury
    with dissolve
    
    
    show agnes at left
    with dissolve

    a "Je ne sais plus ce que j'avais prévu aujourd'hui."

    a "Ce n'est pas grave, je n'ai qu'a aller me balader dans la forêt."
    a "Devrais-je prendre le chemin long ou court ?"
    
    menu:

        "Chemin Long":
            a "j'espère que ça ne sera pas trop long"
            jump choice1_Long

        "Chemin Court":
            a "ça devrait aller par là"
            jump choice1_Court

    label choice1_Long:

        scene black
        show agnes at right
        $ mallaury_eat_apple = False
         
        a "Je ne me rappelais pas que ce chemin était si long, je n'en peux plus {i} halètement {/i}"

        b "Ho mais est ce que ce ne serait pas ma magnifique Agnès"

        a "Haaa... eeeh bonjour baron Vureloi.. vous pro-profité du-du beau temps é-également..."

        b "Pas de besoin de me vouvoyer, nous sommes quand même assez proche"

        a "ooh oui oui oui vous.. fin tu as raison... "

        a "{i} Juste le voir me répugne au plus haut point, j'ai envie de vomir quand je vois ce pourceau, il faut vite que je parte {/i}"

        a "{i} Je ne veux plus jamais revivre ça, se sentiment d'impuissance,.... plus jamais {/i}"

        scene bc_fond

        m " je suis trop beau, je suis tellement beau que seul Arnaud pourrait me mettre 2 claque"

        m " vous ne me croyez pas ? regarder le "    

        show arnaud at top
        with Dissolve(5.0)
        

        jump choice_done

    label choice1_Court:

        scene black
        show agnes at left
        show mallaury at offscreenright

        $ mallaury_eat_apple = True

        m "{i}Agnes se balade dans la forêt avant de croiser une vieille dame.{/i}"
        pause 0.5

        show mallaury at right with moveinleft
        pause 0.5
        show agnes at upCharacter
        pause 0.3
        show mallaury at right

        m "AGNES ??? MAIS TU FAISAIS DES CHOSES LÀ-BAS !?"

        jump choice_done



    label choice_done:

    scene bc_fond
    show agnes at left

    a "Enfin rentrée"

    m "blabla blabla"

    
    if mallaury_eat_apple == True:
        a "tu aurais pu me laisser un morceau de pomme"
    
    m "allons par là-bas"
       
    return