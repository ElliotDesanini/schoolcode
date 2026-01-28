# Bildbehandling och internetteknik

> prov 30-01-2026.  
> lektioner // - //

handlar om hur vebsidor hanterar bilder, vilka bildformat det finns, och vad de är bra för. saker som raster vs vector bilder, DNS (Domain Name Service/System),  

## Bildbehandling

### fil format

#### raster (bitmap)
en raster fil lagrar bilder som **rutnät av pixlar**, som har värden för färg och ibland transparans. 

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
- **Progressiv rendering** -> kalité blir bättre när sida laddar

bra för: foton, landskap och porträtt

##### .webp
_Web Picture Format_ (ny och utvecklad av Google)

- **alfakanal** med 0 - 100% transparans per pixel
- både **lossy** och **förlustfri** kompression
- svår att **redigera** -> tappar kvalité
- **mindre** än jpeg och png for **samma kvalité**
- can ha **animationer** med **24-bit färg** och **alfakanal**

bra för: foton, webbplatsgrafik, transparenta bilder och animerat innehåll

##### .gif
_Grapgic Interchange Format_

- **förlustfri** kompression
- **animation** med **8-bit färg** och **1-bit transparans**
- liten filstorlek
- nästan **alla** applikationer har stöd (sociala media, websidor, email, etc)

bra för: små animationer, memes, instruktioner (how-to)

##### .bmp
_Bitmap_ (Windows)


#### vector


##### .svg
_Scalable Vector Graphics_


## internetteknik