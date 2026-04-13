# Bildbehandling och internetteknik


> prov 30-01-2026.  
> lektioner // - //


handlar om hur webbsidor hanterar bilder, vilka bildformat det finns, och vad de är bra för. saker som raster vs vektor bilder, DNS (Domain Name Service/System),  


## Bildbehandling


### filformat


#### raster (bitmap)
en rasterfil lagrar bilder som **rutnät av pixlar**, som har värden för färg och ibland transparens.


bra för: foton, målningar, konst, komplicerade bilder, detaljer


- bra för **många detaljer** och **färg skiftning** (foton)
- **tappar detalj** om man **zoomar in**


##### .png
_Portable Network Graphics_


- **större filer** för **högre kvalité**
- **alfakanal** med 0 - 100% transparans per pixel
- **förlustfri** kompression
- lätt att **redigera** -> förlorar ingen kvalité


bra för: loggor, UI, skarpa hörn/linjer, konst & illustrationer


##### .jpeg
_Joint Photographic Experts Group_


- **lossy** kompression -> stort **minskad filstorlek**
- 24-bit färg men **ingen transparans**
- bra med **färg gradienter**
- lagrar **meta data**
- **progressiv rendering** -> kalité blir bättre när sida laddar


bra för: foton, landskap och porträtt


##### .webp
_Web Picture Format_ (ny och utvecklad av Google)


- **alfakanal** med 0 - 100% transparans per pixel
- både **lossy** och **förlustfri** kompression
- svår att **redigera** -> tappar kvalité
- **mindre** än jpeg och png for **samma kvalité**
- can ha **animationer** med **24-bit färg** och **alfakanal**


bra för: foton, webbplats grafik, transparenta bilder och animerat innehåll


##### .gif
_Graphic Interchange Format_


- **förlustfri** kompression
- **animation** med **8-bit färg** och **1-bit transparans**
- liten filstorlek
- nästan **alla** applikationer har stöd (sociala media, websidor, email, etc)


bra för: små animationer, memes, instruktioner (how-to)


##### .bmp
_Bitmap_ (Windows)


- **ingen kompression**  
    -> hög **kvalité**  
    -> stora **filer**
- 24-bit färg
- lätt att **redigera**


bra för: redigering


#### vektor
vektorbilder beskriver linjer, färger, punkter och kurvor genom **matematiska definitioner**, inte pixler.


- skarp **kvalité** oavsätt storlek.
- **mindre filstorlek** -> snabbare
- svårt med **foton och detaljer**
- svårare att **redigera**


bra för: logotyper, ikoner, typografi, simpla illustrationer


##### .svg
_Scalable Vector Graphics_


- skrivs i **XML** (Extensible Markup Language) code
- kan **animeras** och **förendras** med **CSS**


för att använda i HTML behöver man **encoding** och **xmlns (XML Namespace)**:
```
<?xml version="1.0" encoding="utf-8"?>
<svg xmlns='http://www.w3.org/2000/svg'></svg>
```
sedan kan filen användas med img:
```
<img src="bild.svg" />
```


### optimera bilder


#### upplösning


upplösningen av en bild borde korrelera med hur **stor den är på skärmen**.


liten bild -> detaljer inte nödvändiga -> liten fil  
stor/fokus bild -> detaljer nödvändiga -> stor fil


#### filstorlek


filstorlek är viktigt att **minimera**. om sidan har för många stora filer påverkar det sidans **laddningstid**.


#### filformat


anpassa filformat efter syfte, och samtidigt håll **filstorlek** och **upplösning** i minne.


transparens är nödvändigt -> .png  
ladda in många detaljer -> .jpeg  
etc


### bild licensiering    


## internetteknik

