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

default mallaury_eat_apple = False


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
    yalign 1.0
    yoffset -50
    linear 0.1
    xzoom 1.0

transform NflipCharacter:
    yalign 1.0
    yoffset -50
    linear 0.1
    xzoom -1.0


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
        play music "ambience_foret.mp3" fadeout 1.0
        show agnes_neutre at left
         
        a "Je ne me rappelais pas que ce chemin était si long, je n'en peux plus.. {i} halètement {/i}"
        
        show pervers_neutre at NflipCharacter, right  

        b "Oh mais ne serait-ce pas ma magnifique Agnès?"

        a "Haaa... euh bonjour baron Vureloi.. vous pro-profitez du-du beau temps é-également...?"

        hide agnes_neutre
        show agnes_gene at left 

        b "Pas besoin de me vouvoyer, nous sommes quand même assez proches"

        a "Ah, oui vous.. enfin tu as raison..."

        a "{i} Juste le voir me répugne au plus haut point, j'ai envie de vomir quand je vois ce pourceau, il faut vite que je parte {/i}"

        a "{i} Je ne veux plus jamais revivre ça, ce sentiment d'impuissance,.... plus jamais {/i}"

        hide pervers_neutre
        hide agnes_gene
        show pervers_horny at PflipCharacter, right
        show agnes_peur at left

        b "Que se passe-t-il ? tu n'as pas l'air bien ? Si tu le souhaites, je peux te raccompagner."
        b "Tu peux même passer chez moi. J'ai un superbe médecin qui travaille pour moi."

        a "{size=-15}Oh je ne voudrais pas m'imposer, ne vous tra- ne te tracasse pas pour moi je vais rentrer, j'ai sûrement besoin d'un bon repas et je me sentirai bien mieux.{/size}"

        a "{size=-10}Une très belle soirée.{/size}"

        b "Une magnifique soirée à toi aussi, au plaisir de pouvoir réapprécier ta compagnie."

        scene placemarchenuit_scene with dissolve
        show mallaury_neutre at left
        with moveinleft

        stop music fadeout 1.0
        play music "ambience_forge.mp3" fadein 1.0

        m "Me voilà enfin arrivé, que vais-je acheter de beau ?"

        show marchand_neutre at NflipCharacter, right
        with moveinright
        ma "Vraiment désolé, mais vous arrivez trop tard.."

        m "Ah bon, vous avez déjà fini ?"

        ma "Oui, vous devriez venir quand le soleil se trouve au zénith, c'est le moment le plus animé."

        m "Merci du conseil l'ami !"
        m "Je pensais être parti assez tôt, j'ai dû prendre trop de temps à m'admirer dans le miroir."
        m "Après il est difficile de ne pas m'admirer."
        hide mallaury_neutre
        show mallaury_vaniteux

        ma "Je vois que vous avez une haute estime de vous même."
        
        m "Il est vrai, mais n'est vous pas d'accord ?"
        m "Vous ne me trouvez pas beau ?"
        hide marchand_neutre
        show marchand_hesitant at right, NflipCharacter
        
        ma "Beau ?"

        m "Oui beau tel un chant de ménéstrel sous la lune."

        ma "Comment dire..."
        ma "J'aurais juste employé un autre terme pour décrire votre beauté voilà tout."

        hide mallaury_vaniteux
        show mallaury_heureux
        m "Je comprends votre stupéfaction, choisir un seul mot pour qualifier mon immense beauté est compliqué."

        ma "Mmmm.. on va dire ça oui.."
        ma "Je vais devoir vous laisser, bonne journée à la plus belle personne."
        hide marchand_hesitant
        show marchand_neutre at right

        m "Merci beaucoup mon brave ! Une excellente journée à vous aussi"

        jump choice_done

    label choice1_Court:

        scene foret_scene with dissolve
        play music "ambience_foret.mp3" fadeout 1.0
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

        v "{b}Hé, toi là bas !{/b}"

        show agnes_peur at NflipCharacter
        pause 0.5
        show agnes_peur at PflipCharacter
        with move


        "{i}Agnes regarde autour d'elle{/i}"
        pause 0.5
        
        a "Moi ? C'est à moi que vous parlez madame ?"

        v "Qui veux-tu que ce soit d'autre SALE TRUANDE"    

        a "Mais !?!?! Je ne vous permet pas qu'est ce qui vous prend ??"

        v "C'est mérité espèce de PUTERELLE"
        v "Tu penses que je ne t'ai pas vu la dernière fois ? Parler avec mon mari avec une telle familiarité ???"

        a "Du calme Madame, je ne connais même pas votre mari."

        v "Si je t'ai vu avec ! Au vu de ta familiarité avec lui tu dois être sa maîtresse. Je vous ai vu il y a quelques jours près d'ici."

        a "Je ne vois pas du tout de quoi vous parlez..."
        a "C'est la première fois que je passe par ici donc ça ne pouvait pas être moi. "

        v "SI JE T'AI VU DE MES PROPRES YEUX !!!!!"

        a "Heeein..? {i} elle commence sacrément à me faire peur {/i}"
        a "{size=-5} Je vais vous laisser Madame, au revoir et bonne journée..{/size}"

        v "QUE JE NE TE VOIS PLUS JAMAIS PAR ICI !"

        scene placemarchejour_scene with dissolve
        show mallaury_neutre at left
        with moveinleft

        stop music fadeout 1.0
        play music "ambience_forge.mp3" fadein 1.0

        m "Me voilà enfin arrivé, que vais-je acheter de beau ?"

        ma "Bonjour ! Venez voir mes magnifiques produits."
        
        show marchand_neutre at NflipCharacter, right
        with moveinright


        m "Bonjour l'ami, qu'avez vous à me proposer ?"

        ma "Des fruits, des légumes et du pain."

        m "Tout ça m'a l'air très bon."
        m "{i}j'hésite... devrais-je prendre des pommes ?{/i}"

        menu:
            "Oui":
                $ mallaury_eat_apple = True
                m "Je vais vous prendre des pommes"
                hide mallaury_neutre
                show mallaury_heureux at left

                ma "Très bon choix, c'est bon pour la ligne !"
                ma "Et voici, ça vous fera 5 pièces de cuivre."
                
                m "Et voilà, merci beaucoup mon brave ! Une excellente journée à vous aussi."

                hide marchand_neutre
                show marchand_fourbe at right
                hide mallaury_heureux
                with dissolve
                ma "{i}J'adore augmenter mes prix, ça lui apprendra à {alpha=.5}cette riche{/alpha}{/i}"

            
            "Non":
                $ mallaury_eat_apple = False

                m "Je ne vais rien vous prendre, bonne journée."

                ma "Pas de soucis, bonne journée."


        jump choice_done



    label choice_done:

    scene bc_fond with dissolve
    show agnes_fatigue at left

    a "Je suis crevée."

    show gustave_neutre at right
    with moveinright
    g "Bonsoir Agnès, le dîner est servi. Voulez-vous manger tout de suite ?"
    

    
    if mallaury_eat_apple == True:
        a "Merci beaucoup Gustave mais je n'ai pas très faim."

        g "Avez-vous déjà mangé ?"

        a "Non je n'ai juste pas faim. Mais merci d'avoir tout préparé vous êtes un amour !"
        a "Je vais aller me coucher je suis exténuée."

        g "Reposez vous bien Madame."
    elif mallaury_eat_apple == False:
        a "Oui merci, je meurs de faim."

        g "Vous avez l'air d'avoir apprécié le repas."

        a "Oui c'était succulant ! Un grand merci à toi Gustave !"

        g "Avec plaisir."

        a "Je vais aller me coucher je suis exténuée."

        g "Reposez vous bien Madame."
    
    scene chambreagnes_scene with dissolve

    m "{i}Baille{/i} Encore une bonne nuit de sommeil de passée."

    m "Je me sens motivé, aujourd'hui je vais sortir de ce pas !"

    menu:
        "Aller au Marché":
            jump choice2_marcher

        "Aller à la Forge":
            jump choice2_forgeron

    label choice2_marcher:

        jump choice2_done


    label choice2_forgeron:

        scene placemarchejour_scene
        with dissolve
        
        show mallaury_heureux at left
        with moveinleft
        m "Bonjour mon brave !"

        show forgeron_neutre at right, NflipCharacter
        f "Bonjour, que puis-je faire pour vous ?"

        m "J'aimerais forger une épee ! "
        
        f "Je vois. Il va me falloir le plus d'indications possibles pour faire l'épee qui vous convient le mieux."

        m "Je pense qu'on s'est mal compris, je voudrais forger l'épée moi même."

        f  "Vous même ?!?"
        hide forgeron_neutre
        show forgeron_ incomprehension at right, NflipCharacter
        f "Ce n'est pas raisonable, vous n'avez ni les compétences ni la force pour réaliser cela."

        m "Pardon ?!?!"
        m "Je ne vous permet d'insulter ma force."

        f "Du calme, pas besoin d'en faire un drame."

        m "Si ? je vais vous couper votre langue de vipère !"
        m "Regardez !"

        f "NON LÂCHEZ ÇA !!!!"

        "{i}Mallaury tente de prendre un marteau pour taper sur l'enclume mais dans sa précipitation, se brûle{/i}"
        

        
        jump choice2_done

    label choice2_done:
        
        scene bucher_scene
    return