import streamlit as st
import random as rand

st.set_page_config(layout="wide", page_title="Random Song Selector", page_icon="🎵")


def happy():
    a1 = "'Happy' by Pharrell Williams"
    a2 = "'Can't Stop the Feeling!' by Justin Timberlake"
    a3 = "'Uptown Funk' by Mark Ronson ft. Bruno Mars"
    a4 = "'Dance Monkey' by Tones and I"
    a5 = "'Shape of You' by Ed Sheeran"
    a6 = "'Despacito' by Luis Fonsi ft. Daddy Yankee"
    a7 = "'Cheap Thrills' by Sia ft. Sean Paul"
    a8 = "'I Wanna Dance with Somebody' by Whitney Houston"
    a9 = "'Ghungroo' from the movie War"
    a10 = "'Dil Dhadakne Do' from the movie Zindagi Na Milegi Dobara"
    a11 = "'Aankh Marey' from the movie Simmba"
    a12 = "'Dil Dooba' from the movie Khakee"
    a13 = "'Dance Basanti' from the movie Ungli"
    a14 = "'Nashe Si Chadh Gayi' from the movie Befikre"
    a15 = "'Dance Pe Chance' from the movie Rab Ne Bana Di Jodi"

    ch = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]

    choice = rand.sample(ch, 5)
    return choice


def sad():
    a1 = "'Someone Like You' by Adele"
    a2 = "'Hurt' by Johnny Cash"
    a3 = "'Channa Mereya' from the movie Ae Dil Hai Mushkil"
    a4 = "'Nothing Compares 2 U' by Sinéad O'Connor"
    a5 = "'Tum Hi Ho' from the movie Aashiqui 2 "
    a6 = "'Hallelujah' by Jeff Buckley"
    a7 = "'Fix You' by Coldplay"
    a8 = "'Teri Galiyan' from the movie Ek Villain "
    a9 = "'Skinny Love' by Bon Iver"
    a10 = "'Kabira' from the movie Yeh Jawaani Hai Deewani"
    a11 = "'Someone You Loved' by Lewis Capaldi"
    a12 = "'Tujhe Bhula Diya' from the movie Anjaana Anjaani"
    a13 = "'Everybody Hurts' by R.E.M"
    a14 = "'Kal Ho Naa Ho' from the movie Kal Ho Naa Ho "
    a15 = "'Mad World' by Gary Jules"

    ch = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]

    choice = rand.sample(ch, 5)
    return choice


def broken():
    a1 = "'Tujhe Bhula Diya' from the movie Anjaana Anjaani"
    a2 = "'Hurt' by Johnny Cash"
    a3 = "'Cold' by Maroon 5"
    a4 = "'Nothing Compares 2 U' by Sinéad O'Connor"
    a5 = "'Channa Mereya' from the movie Ae Dil Hai Mushkil"
    a6 = "'Someone Like You' by Adele"
    a7 = "'Fix You' by Coldplay"
    a8 = "'Teri Galiyan' from the movie Ek Villain "
    a9 = "'Skinny Love' by Bon Iver"
    a10 = "'Hurt' by Johnny Cash"
    a11 = "'Someone You Loved' by Lewis Capaldi"
    a12 = "'Tum Hi Ho' from the movie Aashiqui 2"
    a13 = "'Talking To The Moon' by Bruno Mars"
    a14 = "'Kal Ho Naa Ho' from the movie Kal Ho Naa Ho "
    a15 = "'Somebody That I used To Know' by Gotye"

    ch = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]

    choice = rand.sample(ch, 5)
    return choice


def romantic():
    a1 = "'Perfect' by Ed Sheeran"
    a2 = "'Tum Hi Ho' from the movie Aashiqui 2"
    a3 = "'Can't Help Falling in Love' by Elvis Presley"
    a4 = "'Enna Sona' from the movie OK Jaanu"
    a5 = "'Thinking Out Loud' by Ed Sheeran"
    a6 = "'Gerua' from the movie Dilwale"
    a7 = "'Unchained Melody' by The Righteous Brothers"
    a8 = "'Bolna' from the movie Kapoor & Sons"
    a9 = "'I Will Always Love You' by Whitney Houston"
    a10 = "'Tum Se Hi' from the movie Jab We Met"
    a11 = "'Endless Love' by Diana Ross & Lionel Richie"
    a12 = "'Raabta' from the movie Agent Vinod"
    a13 = "'At Last' by Etta James"
    a14 = "'Pehli Nazar Mein' from the movie Race"
    a15 = "'La Vie En Rose' by Edith Piaf"

    ch = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]

    choice = rand.sample(ch, 5)
    return choice


def energetic():
    a1 = "'Don't Stop Believin' by Journey"
    a2 = "'Jai Ho' from the movie Slumdog Millionaire"
    a3 = "'Eye of the Tiger' by Survivor"
    a4 = "'Dhoom Machale' from the movie Dhoom"
    a5 = "'Can't Hold Us' by Macklemore & Ryan Lewis ft. Ray Dalton"
    a6 = "'Zinda' from the movie Bhaag Milkha Bhaag"
    a7 = "'Shut Up and Dance' by Walk the Moon"
    a8 = "'Dil Chahta Hai' from the movie Dil Chahta Hai"
    a9 = "'We Will Rock You' by Queen"
    a10 = "'Salaam Namaste' from the movie Salaam Namaste"
    a11 = "'Uptown Funk' by Mark Ronson ft. Bruno Mars"
    a12 = "'Dance Pe Chance' from the movie Rab Ne Bana Di Jodi"
    a13 = "'I Gotta Feeling' by The Black Eyed Peas"
    a14 = "'Aaj Ki Raat' from the movie Don"
    a15 = "'Happy' by Pharrell Williams"

    ch = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]

    choice = rand.sample(ch, 5)
    return choice

def rock():
    a1 = "'Stairway to Heaven' by Led Zeppelin"
    a2 = "'Bohemian Rhapsody' by Queen"
    a3 = "'Hotel California' by Eagles"
    a4 = "'Smells Like Teen Spirit' by Nirvana"
    a5 = "'Sweet Child o' Mine' by Guns N' Roses"
    a6 = "'Back in Black' by AC/DC"
    a7 = "'Imagine' by John Lennon"
    a8 = "'Livin' on a Prayer' by Bon Jovi"
    a9 = "'November Rain' by Guns N' Roses"
    a10 = "'Wish You Were Here' by Pink Floyd"
    a11 = "'Don't Stop Believin'' by Journey"
    a12 = "'Dream On' by Aerosmith"
    a13 = "'Free Fallin'' by Tom Petty"
    a14 = "'The Sound of Silence' by Simon & Garfunkel"
    a15 = "'Highway to Hell' by AC/DC"

    ch = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]

    choice = rand.sample(ch, 5)
    return choice

def pop():
    a1 = "'Billie Jean' by Michael Jackson"
    a2 = "'Shape of You' by Ed Sheeran"
    a3 = "'Uptown Funk' by Mark Ronson ft. Bruno Mars"
    a4 = "'Dance Monkey' by Tones and I"
    a5 = "'Despacito' by Luis Fonsi ft. Daddy Yankee"
    a6 = "'Cheap Thrills' by Sia ft. Sean Paul"
    a7 = "'I Wanna Dance with Somebody' by Whitney Houston"
    a8 = "'Happy' by Pharrell Williams"
    a9 = "'Can't Stop the Feeling!' by Justin Timberlake"
    a10 = "'Dance Pe Chance' from the movie Rab Ne Bana Di Jodi"
    a11 = "'La Vie En Rose' by Edith Piaf"
    a12 = "'Mad World' by Gary Jules"
    a13 = "'Perfect' by Ed Sheeran"
    a14 = "'Thinking Out Loud' by Ed Sheeran"
    a15 = "'Enna Sona' from the movie OK Jaanu"

    ch = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]

    choice = rand.sample(ch, 5)
    return choice

def hip_hop():
    a1 = "'Lose Yourself' by Eminem"
    a2 = "'Empire State of Mind' by Jay-Z ft. Alicia Keys"
    a3 = "'In da Club' by 50 Cent"
    a4 = "'Sicko Mode' by Travis Scott"
    a5 = "'HUMBLE.' by Kendrick Lamar"
    a6 = "'Hotline Bling' by Drake"
    a7 = "'Old Town Road' by Lil Nas X ft. Billy Ray Cyrus"
    a8 = "'Bodak Yellow' by Cardi B"
    a9 = "'Savage' by Megan Thee Stallion"
    a10 = "'WAP' by Cardi B ft. Megan Thee Stallion"
    a11 = "'God's Plan' by Drake"
    a12 = "'Life Goes On' by BTS"
    a13 = "'The Box' by Roddy Ricch"
    a14 = "'Rockstar' by Post Malone ft. 21 Savage"
    a15 = "'Suge' by DaBaby"

    ch = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]

    choice = rand.sample(ch, 5)
    return choice

def country():
    a1 = "'Take Me Home, Country Roads' by John Denver"
    a2 = "'Friends in Low Places' by Garth Brooks"
    a3 = "'The Dance' by Garth Brooks"
    a4 = "'Wagon Wheel' by Old Crow Medicine Show"
    a5 = "'Before He Cheats' by Carrie Underwood"
    a6 = "'Dirt Road Anthem' by Jason Aldean"
    a7 = "'I Hope You Dance' by Lee Ann Womack"
    a8 = "'Chicken Fried' by Zac Brown Band"
    a9 = "'Cruise' by Florida Georgia Line"
    a10 = "'Jolene' by Dolly Parton"
    a11 = "'Mama's Broken Heart' by Miranda Lambert"
    a12 = "'Tennessee Whiskey' by Chris Stapleton"
    a13 = "'The House That Built Me' by Miranda Lambert"
    a14 = "'Body Like a Back Road' by Sam Hunt"
    a15 = "'Colder Weather' by Zac Brown Band"

    ch = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]

    choice = rand.sample(ch, 5)
    return choice

def indie():
    a1 = "'Fluorescent Adolescent' by Arctic Monkeys"
    a2 = "'Take Me Out' by Franz Ferdinand"
    a3 = "'Pumped Up Kicks' by Foster the People"
    a4 = "'Ho Hey' by The Lumineers"
    a5 = "'Electric Feel' by MGMT"
    a6 = "'Mr. Brightside' by The Killers"
    a7 = "'Kids' by MGMT"
    a8 = "'Feel Good Inc.' by Gorillaz"
    a9 = "'1901' by Phoenix"
    a10 = "'Do I Wanna Know?' by Arctic Monkeys"
    a11 = "'Somebody That I Used to Know' by Gotye"
    a12 = "'Sweater Weather' by The Neighbourhood"
    a13 = "'Little Talks' by Of Monsters and Men"
    a14 = "'Breezeblocks' by Alt-J"
    a15 = "'The Cave' by Mumford & Sons"

    ch = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]

    choice = rand.sample(ch, 5)
    return choice

def soul():
    a1 = "'I Heard It Through the Grapevine' by Marvin Gaye"
    a2 = "'Respect' by Aretha Franklin"
    a3 = "'Let's Stay Together' by Al Green"
    a4 = "'A Change Is Gonna Come' by Sam Cooke"
    a5 = "'Lean on Me' by Bill Withers"
    a6 = "'(Sittin' On) The Dock of the Bay' by Otis Redding"
    a7 = "'My Girl' by The Temptations"
    a8 = "'Stand by Me' by Ben E. King"
    a9 = "'I Got You (I Feel Good)' by James Brown"
    a10 = "'Chain of Fools' by Aretha Franklin"
    a11 = "'Ain't No Mountain High Enough' by Marvin Gaye & Tammi Terrell"
    a12 = "'At Last' by Etta James"
    a13 = "'What's Going On' by Marvin Gaye"
    a14 = "'Try a Little Tenderness' by Otis Redding"
    a15 = "'Lovely Day' by Bill Withers"

    ch = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]

    choice = rand.sample(ch, 5)
    return choice


st.sidebar.title('Random Song Selector')
option = st.text_input("Enter your mood")
if st.button("Generate Playlist"):
    option.lower()
    if "happy" in option:
        playlist = happy()
        st.sidebar.write("\n\n".join(playlist))
        i1 = "https://thumbs.dreamstime.com/z/happy-fresh-summer-girl-pastel-colours-style-s-aesthetic-flowers-bloom-positive-mood-playful-fashion-trendy-accessories-street-188290792.jpg"
        st.image(i1, use_column_width=True)
        
    elif "sad" in option:
        playlist = sad()
        st.sidebar.write("\n\n".join(playlist))
        i2 = "https://m.media-amazon.com/images/I/41SuW3Z9o-L._UXNaN_FMjpg_QL85_.jpg"
        st.image(i2, use_column_width=True)

    elif "broken" in option:
        playlist = broken()
        st.sidebar.write("\n\n".join(playlist))
        i3 = "https://wallpapers.com/images/hd/she-s-broken-mood-off-nta66f2ic9571xl9.jpg"
        st.image(i3, use_column_width=True)
            
    elif "romantic" in option:
        playlist = romantic()
        st.sidebar.write("\n\n".join(playlist))
        i4 = "https://media.assettype.com/freepressjournal/2023-02/efb62ed6-f876-4968-aa19-c0cca08c99fa/pyaar_hua.jpg"
        st.image(i4, use_column_width=True)
        
    elif "energetic" in option:
        playlist = energetic()
        st.sidebar.write("\n\n".join(playlist))
        i5 = "https://c.saavncdn.com/128/Best-Driving-Rock-Music-Motorcycle-Riding-Road-Trip-The-Journey-Ahead-English-2018-20180417073353-500x500.jpg"
        st.image(i5, use_column_width=True)

    elif "rock" in option:
        playlist = rock()
        st.sidebar.write("\n\n".join(playlist))
        i6 = "https://www.shutterstock.com/shutterstock/photos/2011011410/display_1500/stock-vector-rock-n-roll-punk-music-doodle-set-graffiti-tattoo-hand-drawn-sticker-text-skull-heart-skate-2011011410.jpg"
        st.image(i6, use_column_width=True)
        
    elif "pop" in option:
        playlist = pop()
        st.sidebar.write("\n\n".join(playlist))
        i7 = "https://lobopopart.com.br/wp-content/uploads/2016/09/Arte-Quarentena.jpg"
        st.image(i7, use_column_width=True)
    
    elif "country" in option:
        playlist = country()
        st.sidebar.write("\n\n".join(playlist))
        i8 = "https://i.pinimg.com/564x/a3/03/02/a30302da6060b6bea4c2c58d36f0dd49.jpg"
        st.image(i8, use_column_width=True)
        
    elif "hiphop" in option:
        playlist = hip_hop()
        st.sidebar.write("\n\n".join(playlist))
        i9 = "https://i.pinimg.com/1200x/2d/40/31/2d403139f7117c0fad6387d1d30b562b.jpg"
        st.image(i9, use_column_width=True)
        
    elif "indie" in option:
        playlist = indie()
        st.sidebar.write("\n\n".join(playlist))
        i10 = "https://img.freepik.com/free-vector/hand-drawn-indie-music-illustration_23-2149676429.jpg"
        st.image(i10, use_column_width=True)
    
    elif "soul" in option:
        playlist = soul()
        st.sidebar.write("\n\n".join(playlist))
        i11 = "https://static.displate.com/280x392/displate/2023-05-07/126cc45d455ce3093f8cdce66a55bc59_c55b6f28c13008e56c4132f060e5d7e0.jpg"
        st.image(i11, use_column_width=True)