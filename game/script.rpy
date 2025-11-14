# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define a = Character(_('Agnes'),color="#123e5f")
define m = Character(_('Mallaury'),color="#149a5e")
define g = Character(_('Gustave'), color="#3e49ec")
define b = Character(_('Baron Vureloi'),color="#4a6c8d")
define v = Character(_('Veille folle'), color= "#d70505")
define ma = Character(_('Marchand'), color= "#5c0764")
define f = Character(_('Forgeron'), color= "#857c86d9")

define al = Character(_('TOUS'), color= "#ff0000d9")

default mallaury_eat_apple = False
default see_Baron_Forest = False
default go_marche = False
default go_Forge = False
default chemin_court = False


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

# Une "image" blanche pleine écran
image flash_white = Solid("#f95050")

# Un transform ATL qui fait apparaître puis disparaître la flash
transform flash_anim:
    alpha 0.0
    linear 0.04 alpha 1.0    # montée rapide
    linear 0.12 alpha 0.0    # descente (on voit l'impact puis retour)

transform leftish:
    xalign 0.25
    yalign 1.0

transform centerish:
    xalign 0.5
    yalign 1.0

transform rightish:
    xalign 0.75
    yalign 1.0



# Le jeu commence ici
label start:
    
    show screen cadre_hud
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
        with dissolve
        play music "ambiance_foret.mp3" fadeout 1.0
        show agnes_neutre at left
         
        a "Je ne me rappelais pas que ce chemin était si long, je n'en peux plus.. {i} halètement {/i}"
        
        show pervers_neutre at right  

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
        show pervers_horny at right
        show agnes_peur at left

        b "Que se passe-t-il ? tu n'as pas l'air bien ? Si tu le souhaites, je peux te raccompagner."
        b "Tu peux même passer chez moi. J'ai un superbe médecin qui travaille pour moi."

        a "{size=-15}Oh je ne voudrais pas m'imposer, ne vous tra- ne te tracasse pas pour moi je vais rentrer, j'ai sûrement besoin d'un bon repas et je me sentirai bien mieux.{/size}"

        a "{size=-10}Une très belle soirée.{/size}"

        b "Une magnifique soirée à toi aussi, au plaisir de pouvoir réapprécier ta compagnie."

        $ see_Baron_Forest = True
        scene placemarchenuit_scene with dissolve
        show mallaury_neutre at left
        with moveinleft

        stop music fadeout 1.0
        play music "ambiance-village-sans-marche-loopable.mp3" fadein 1.0

        m "Me voilà enfin arrivé, que vais-je acheter de beau ?"

        show marchand_neutre at right
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
        
        m "Il est vrai, mais n'êtes vous pas d'accord ?"
        m "Vous ne me trouvez pas beau ?"
        hide marchand_neutre
        show marchand_hesitant at right
        
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
        play music "ambiance_foret.mp3" fadeout 1.0
        show agnes_heureuse at left
        show vieille_neutre at offscreenright

        $ chemin_court = True

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
        play music "ambiance-village-avec-marche-loopable.mp3" fadein 1.0

        m "Me voilà enfin arrivé, que vais-je acheter de beau ?"

        show marchand_neutre at right
        with moveinright
        ma "Bonjour ! Venez voir mes magnifiques produits."

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

    play music "ambiance_chateau.mp3" fadeout 1.0
    scene bc_fond with dissolve
    show agnes_fatigue at left

    a "Je suis fatiguée"

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
    
    scene chambreagnes_scene with Dissolve(2)
    
    show mallaury_baille
    m "{i}Baille{/i} Encore une bonne nuit de sommeil de passée."

    m "Je me sens motivé, aujourd'hui je vais sortir de ce pas !"

    hide mallaury_baille
    menu:
        "Aller au Marché":
            jump choice2_marcher

        "Aller à la Forge":
            jump choice2_forgeron

    label choice2_marcher:

        scene placemarchejour_scene
        play music "ambiance-village-avec-marche-loopable.mp3" fadeout 1.0

        $ go_marche = True

        if see_Baron_Forest == True:
            show mallaury_neutre at left
            with dissolve
            m "Me revoilà , cette fois ci à temps !"

            show pervers_neutre at right
            with moveinright
            b "Quelle chance de vous revoir !"
        elif see_Baron_Forest == False:
            show mallaury_neutre at left
            with dissolve
            m "Me revoilà, cette fois-ci j'ai envie de voir de beaux objets."

            show pervers_neutre at right
            with moveinright
            b "Quelle chance de tomber sur toi en ce lieu, ta compagnie m'est toujours très agréable."
        
        m "Désolé monsieur mais nous connaissons-nous ?"

        b "?!?!?!?! Comment ça ?"

        m "Je ne vous ai jamais vu de ma vie."
        hide mallaury_neutre
        show mallaury_colere at left

        b "Le soleil doit te jouer des tours, je suis le baron Vureloi."

        m "Je vous prierai de ne pas me tutoyer monsieur Vureloi."

        b "Vous me fendez le coeur, je ne peux subir cet affront plus longtemps..."
        b "Je pensais vraiment que notre relation était unique..."
        b "Passe une belle journée.."
        b "{i}Agnès...{/i}"

        hide mallaury_colere
        with dissolve
        hide pervers_neutre
        with dissolve
        jump choice2_done


    label choice2_forgeron:

        scene placemarchejour_scene
        play music "ambiance_forge.mp3" fadeout 1.0
        with dissolve
        
        show mallaury_heureux at left
        with moveinleft
        m "Bonjour mon brave !"

        $ go_Forge = True
        show forgeron_neutre at right
        f "Bonjour, que puis-je faire pour vous ?"

        m "J'aimerais forger une épee ! "
        
        f "Je vois. Il va me falloir le plus d'indications possibles pour faire l'épee qui vous convient le mieux."

        m "Je pense qu'on s'est mal compris, je voudrais forger l'épée moi même."

        f  "Vous même ?!?"
        hide forgeron_neutre
        show forgeron_ incomprehension at right
        f "Ce n'est pas raisonable, vous n'avez ni les compétences ni la force pour réaliser cela."

        m "Pardon ?!?!"
        m "Je ne vous permet pas d'insulter ma force."

        f "Du calme, pas besoin d'en faire un drame."

        m "Si ? je vais vous couper votre langue de vipère !"
        m "Regardez !"

        f "NON LÂCHEZ ÇA !!!!"

        "{i}Mallaury tente de prendre un marteau pour taper sur l'enclume mais dans sa précipitation, se brûle{/i}"
        show flash_white onlayer overlay at flash_anim
        pause 0.5
        hide flash_white onlayer overlay
        hide mallaury_heureux
        show mallaury_douleur

        m "AAAAAAAAAAAAAAAAAAAH !"

        f "MON DIEU !"

        m "Ce.. Ce n'est rien."

        f "Vous rigolez ? Vous venez de vous brûler, aller venez mettre votre main sous l'eau froide."

        m "Arg, merci.."

        hide mallaury_heureux
        with dissolve

        hide forgeron_ incomprehension
        with dissolve
        jump choice2_done

    label choice2_done:
        
        play music "theme_finale.mp3" fadeout 1.0
        show agnes_heureuse at left
        with moveinleft 

        a "Pourquoi me suis-je rendue au marché ?"

        show vieille_neutre at right
        with moveinright
        v "Elle est là cette sorcière !!!"

        if chemin_court == True:
            a "Encore vous ?!"
        elif chemin_court == False:
            a "Qui êtes vous et que me voulez vous ?"
        
        hide agnes_heureuse
        show agnes_peur at left
        a "Laissez moi tranquille à la fin"
        

        v "Ne joue pas au innocente, je ne suis pas la seule à avoir remarqué tes agissements suspects."

        show marchand_hesitant at rightish behind vieille_neutre
        with moveinright

        show forgeron_colere at rightish behind vieille_neutre
        with moveinright

        show pervers_neutre at right behind marchand_hesitant
        with dissolve


        if chemin_court == True:
            hide marchand_hesitant
            show marchand_hesitant
            ma "Cette femme est possédée !"
            hide marchand_hesitant
            show marchand_hesitant at rightish behind vieille_neutre
            with dissolve
        elif go_Forge == True:
            hide forgeron_colere
            show forgeron_colere
            f "Elle est dangereuse !"
            hide forgeron_colere
            show forgeron_colere at rightish behind vieille_neutre
            with dissolve
        if see_Baron_Forest == True:
            hide pervers_neutre
            show pervers_neutre
            b "Un démon a dû prendre possession d'elle..."
            hide pervers_neutre
            show pervers_neutre at right behind marchand_hesitant
            with dissolve


        a "De quoi parlez-vous tous ?"

        show gustave_neutre
        g "Madame... votre comportement m'inquiète de plus en plus ces derniers temps..."

        a "Gustave mais que fais tu là ?"

        g "Je suis avec eux...."
        g "Vous n'imaginez pas à quel point il était difficile pour moi d'accepter cette réalité.."

        a "Gustave... expliquez moi, vous commencez tous à me faire peur !"
        
        g "Un démon a prit possession de vous."
        a "Votre blague est de très mauvais goût..."

        g "Malheureusment ça n'en n'est pas une..."
        g "Tout d'abord, votre comportement change radicalement d'un moment à l'autre."
        g "Quand ce démon prend possession de votre corps, vous ne vous rappelez même pas ce qu'il a fait."

        a "QUOI ?!? Je n'ai aucun problème de mémoire."

        if go_Forge == True:
            hide gustave_neutre
            hide forgeron_colere
            show forgeron_colere
            
            f "Pouvez-vous nous dire où vous vous êtes blessée ? "
            a "Je ne me suis pas blessée. J-je ne comprend plus rien."
            f "Votre main."

            a "{i}Hein ? Depuis quand j'ai cette brûlure ?{/i}"
            hide forgeron_colere
            show forgeron_colere at rightish behind vieille_neutre
            with dissolve
        elif see_Baron_Forest and go_marche == True:
            hide gustave_neutre
            hide pervers_neutre
            show pervers_neutre
            
            b "Combien de fois nous sommes nous vus récément ?"

            a "Nous nous sommes croisés hier en forêt."
            
            b "Je t'ai croisé en forêt mais aussi ce matin."
            a " NON impossible !"
            a "{i}je m'en souviendrais si j'avais croisé ce vieux pourceau{/i}"
            hide pervers_neutre
            show pervers_neutre at right behind marchand_hesitant
            with dissolve
        elif go_marche == True:
            hide gustave_neutre
            hide pervers_neutre
            show pervers_neutre
            
            b "Combien de fois nous sommes nous vus récément ?"
            a "Nous ne nous sommes pas croisé récement."
            b "Je t'ai croisé ce matin."
            a " NON impossible !"
            a "{i}je m'en souviendrais si j'avais croisé ce vieux pourceau{/i}"

            hide pervers_neutre
            show pervers_neutre at right behind marchand_hesitant
            with dissolve
        
        elif mallaury_eat_apple == True:
            hide marchand_neutre
            show marchand_neutre
            g "Vous ne vous souvenez même plus si vous avez mangé."
            g "Vous m'aviez dit ne rien avoir mangé."

            ma "Alors que vous m'avez acheter des pommes et vous les avez mangées !"
            hide marchand_neutre
            show marchand_hesitant at rightish behind vieille_neutre
            hide gustave_neutre

        v "Vous avez des conversations avec des gens et vous ne vous en rappelez même plus !"

        a "J-je.... je.... j-je ne comprend plus rien."

        a "Gustave aidez moi !"

        show gustave_neutre

        g "Je suis à votre service depuis longtemps maintenant, nous vivons à deux dans votre demeure."

        g "Je suis le premier attristé par la situation..."

        g "je prierai en votre mémoire."

        a "QUOI ?!?!"
        
        al "AU BÛCHER !"
        al "DÉMON !"
        v "SORCIÈRE !"

        b "NOUS DEVONS CHÂTIER LE DÉMON QUI EST EN ELLE!"

        a "NON ARRÊTEZ ! LÂCHEZ MOI !"

        hide gustave_neutre
        hide agnes_peur
        hide pervers_neutre
        hide marchand_hesitant
        hide forgeron_colere
        scene scene_bucher_1
        play music "ambiance_bucher.mp3" fadeout 1.0

        m "AAAAAAAAAAAAAAAAAAAAAAH !"

        scene scene_bucher_2

        a "AAAAAAAAAAAAAAAAAAAAAAAH !"

        pause 2.5

        scene chambreagnes_scene 
        with dissolve

        show gustave_neutre

        g "Il ne me reste plus que sa chambre, le dernier souvenir qu'il me reste d'elle..."

        hide gustave_neutre
        show ecranfin
        pause 4.0


    return