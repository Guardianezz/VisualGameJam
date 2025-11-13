# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define a = Character('Agnes',color="#123e5f")
define m = Character('Mallaury',color="#149a5e")
define g = Character('Gustave', color="#3e49ec")
define b = Character('Baron Vureloi',color="#4a6c8d")
define v = Character('Veille folle', color= "#e8dc09")
define ma = Character('Marchand', color= "#5c0764")
define f = Character('Forgeron', color= "#857c86d9")

$ default = mallaury_eat_apple

transform upCharacter:
    #monte le perso
    yoffset -300
    linear 0.1
  
    #le descend
    yoffset 300
    linear 0.1
transform Ucharacter:
    xalign 0.8
    yalign 1.0
    yoffset -300

transform PflipCharacter:
    yoffset 300
    linear 0.1 xzoom 1.0

transform NflipCharacter:
    yoffset 300
    linear 0.1 xzoom -1.0

transform flipAnim:
    parallel:
        linear 0.2 xzoom 0.0
        linear 0.2 xzoom -1.0

# Le jeu commence ici
label start:

    scene bc_fond
    play music "theme_mallaury.mp3" fadeout 1
    show mallaury_neutre at left
    show gustave_neutre at right
    with dissolve

    m "Alors Gustave, qu'allez-vous faire de beau aujourd'hui ?"
    g "Je vais m'occuper de nettoyer le domaine. Et vous que comptez-vous faire ?"

    m "Je ne sais pas encore. Avez vous des suggestions mon cher ?"
    g "Je vous conseille de profiter que le soleil soit à son zénith pour faire un tour au marché, l'air frais vous fera le plus grand bien."
    m "Un grand merci mon très cher Gustave je vais suivre votre conseil ! En route pour le marché !"
    
    hide mallaury_neutre
    hide gustave_neutre
    with dissolve
    
    play music "theme_agnes.mp3" fadeout 1
    show agnes_neutre at left
    with dissolve

    a "Je ne sais plus ce que j'avais prévu aujourd'hui."
    a "Ce n'est pas grave, je n'ai qu'à aller me balader dans la forêt."
    a "Devrais-je faire une longue ou une courte balade ?"
    
    menu:

        "Chemin Long":
            jump choice1_Long

        "Chemin Court":
            jump choice1_Court

    label choice1_Long:

        scene foret_scene
        play music "ambience_foret.mp3"
        show agnes_neutre at left
         
        a "Je ne me rappelais pas que ce chemin était si long, je n'en peux plus.. {i} halètement {/i}"

        
        
        show pervers_neutre at Ucharacter, right
        show pervers_neutre at NflipCharacter   

        b "Oh mais ne serait-ce pas ma magnifique Agnès?"

        a "Haaa... euh bonjour baron Vureloi.. vous pro-profitez du-du beau temps é-également...?"

        b "Pas besoin de me vouvoyer, nous sommes quand même assez proches"

        a "Ah, oui vous.. enfin tu as raison... "

        a "{i} Juste le voir me répugne au plus haut point, j'ai envie de vomir quand je vois ce pourceau, il faut vite que je parte  {/i}"

        a "{i} Je ne veux plus jamais revivre ça, ce sentiment d'impuissance,.... plus jamais {/i}"

        b "Que ce passe t'il ? tu n'as pas l'air bien ? Si tu le souhaite je peux te raccompagné, tu peux même passé chez moi. J'ai un superbe médecin qui travail pour moi."

        a "Ho je ne voudrais pas m'imposer, ne vous tra- ne te tracasse pas pour moi je vais rentré, j'ai surement besoin d'un bon repas et je me sentirais bien mieux."

        a "Une très belle soirée"

        b "Une magnifique soirée à toi aussi, au plaisir de pouvoir réapprécier ta compagnie."

        scene placemarchejour_scene

        m " je suis trop beau, je suis tellement beau que seul Arnaud pourrait me mettre 2 claque"

        
        

        jump choice_done

    label choice1_Court:

        scene foret_scene with dissolve
        play music "ambience_foret.mp3"
        show agnes_heureuse at left
        show vieille_neutre at offscreenright

        

        a "Ce petit chemin est très agréable, il faudrait que j'y passe plus souvent."
        pause 0.5

        show vieille_neutre at right with moveinleft
        pause 0.5
        hide agnes_heureuse
        show agnes_peur at upCharacter
        pause 0.3
        show vieille_neutre at right

        v "{b}Hé   toi    là    bas {/b}"

        show agnes_peur at NflipCharacter
        pause 0.5
        show agnes_peur at PflipCharacter
        with move


        "{i}Agnes regarde autour d'elle{/i}"
        pause 0.5
        
        a "Moi ? C'est à moi que vous parlez madame ?"

        v "Qui veut tu que ce soit d'autre SALE TRUANDE"    

        a "Mais !?!?! je ne vous permet pas qu'est ce qui vous prend ??"

        v "C'est mérité espèce de PUTERELLE"
        v "Tu penses que je ne t'ai pas vu la dernière fois parler avec mon mari avec une tel familiarité ???"

        a "Madame, du calme je ne connais même pas votre mari"

        v "Si je t'ai vu avec, au vu de ta familiarité avec lui tu dois être sa maitresse, je vous ai vu il y a quelque jouer près d'ici."

        a "Je ne vois pas dutout de quoi vous parlez..."
        a "C'est la première fois que je passe par ici donc ça ne pouvais pas être moi "

        v "SI JE T'AI VU DE MES PROPRES YEUX !!!!!"

        a "Heeein..? {i} elle commence sacrément à me faire peur {/i}"
        a "{size=-5} Je vais vous laisser madame aurevoir et bonne journée.. {/size}"

        v "QUE JE NE TE VOIS PLUS JAMAIS PAR ICI"

        scene placemarchejour_scene with dissolve
        show mallaury_heureux with dissolve

        m "Arrive au marché"

        ma "Lui demande si il veut quelque chose"

        m "Est-ce que je prends une pomme ?"

        menu:
            "Oui":
                $ mallaury_eat_apple = True
                m "Je vais vous prendre des pommes"

                ma "gngngng j'augmente mes prix tel un rat"
            
            "Non":
                $ mallaury_eat_apple = False

                m "je ne vais rien prendre"


        jump choice_done



    label choice_done:

    scene bc_fond with dissolve
    show agnes_fatigue at left

    a "Enfin rentrée"

    g "blabla blabla faim ?"

    
    if mallaury_eat_apple == True:
        a "Non merci je n'ai pas faim"

        g "vous avez déjà mangée ?"

        a "non j'ai juste pas faim Zeubi"
        a "je vais aller dodo my bro"

        g "vasy bonne nuit ma gatée"
    else :
        a "j'ai giga faim merci"

        g "bonne appetit"

        a "je vais aller me coucher ciao"
    
    scene chambreagnes_scene with dissolve

    m "Envie de craft mon épée en nétherite ou je l'achète comme quelqu'un de normal ?"

    menu:
        "je suis normal je l'achète":
            jump choice2_marcher

        "je suis un bonhomme moi":
            jump choice2_forgeron

    label choice2_marcher:

        jump choice2_done


    label choice2_forgeron:

        jump choice2_done

    label choice2_done:
        
        scene bucher_scene
    return