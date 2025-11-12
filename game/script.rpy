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

transform NflipCharacter:
    xzoom -1.0

transform PflipCharacter:
    xzoom 1.0

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

        b "Que ce passe t'il ? tu n'as pas l'air bien ? Si tu le souhaite je peux te raccompagné, tu peux même passé chez moi. J'ai un superbe médecin qui travail pour moi."

        a "Ho je ne voudrais pas m'imposer, ne vous tra- ne te tracasse pas pour moi je vais rentré, j'ai surement besoin d'un bon repas et je me sentirais bien mieux."

        a "Une très belle soirée"

        b "Une magnifique soirée à toi aussi, au plaisir de pouvoir réapprécier ta compagnie."

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

        a "Ce petit chemin est très agréable, il faudrait que j'y passe plus souvent."
        pause 0.5

        show mallaury at right with moveinleft
        pause 0.5
        show agnes at upCharacter
        pause 0.3
        show mallaury at right

        m "{b}Hé toi là bas {/b}"

        show agnes at NflipCharacter
        pause 0.3
        show agnes at PflipCharacter
        "{i}Agnes regarde autour d'elle{/i}"
        pause 0.5
        
        a "Moi ? C'est à moi que vous parlez madame ?"

        m "Qui veut tu que ce soit d'autre SALE TRUANDE"

        a "Mais !?!?! je ne vous permet pas qu'est ce qui vous prend ??"

        m "C'est mérité espèce de PUTERELLE"
        m "Tu penses que je ne t'ai pas vu la dernière fois parler avec mon mari avec une tel familiarité ???"

        a "Madame, du calme je ne connais même pas votre mari"

        m "Si je t'ai vu avec, au vu de ta familiarité avec lui tu dois être sa maitresse, je vous ai vu il y a quelque jouer près d'ici."

        a "Je ne vois pas dutout de quoi vous parlez..."
        a "C'est la première fois que je passe par ici donc ça ne pouvais pas être moi "

        m "SI JE T'AI VU DE MES PROPRES YEUX !!!!!"

        a "Heee {i} elle commence sacrément à me faire peur {/i}"
        a "{size=-5} Je vais vous laisser madame aure voir et bonne journée.. {/size}"

        m "QUE JE NE TE VOIS PLUS JAMAIS PAR ICI"

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