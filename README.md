# PropBank Spanish with Ancora + ADESSE
Ideally, this project could become
a Propbank instance editor with improved 
user experience than Jubilee and would include
the connection with ADESSE (in the case of Spanish).
The project also attempts to include a lot more
information found in PropBank's annotation
guidelines to aid the annotator's process.

At the moment, the project can do or has the following:
- obtain all verb instances from AnCora Spanish corpus
- obtain verb senses for specific verb from ADESSE scraping
- obtains a dictionary with verb entries from AnCora and their respective TreeBank objects
- create verb instances
- create frameset instances
- display list of verbs in html webpage
- display verb instances in html webpage
- form to create frameset instance

To run and see -work-in-progress- web interace:
```bash
$ python3 home.py
```

## PropBank Annotation
1. Argument labeling
2. Annotation of modifiers
3. Choosing a sense for the predicate
4. Creating links for empty categories, relative clauses, and reduced relatives

### PropBankAnnotation.json
This file details PropBank's annotation guidelines to
ensure consistency.

## Verbs
```json
{
    "lemma": "sentir",
    "framesets": [
        {
            "id": 123,
            "verb": "sentir.1",
            "comment": "Percibir, notar",
            "roles": {
                "arg0": "Persona que percibe",
                "arg1": "Objeto percibido"
            }
        },
        {
            "id": 124,
            "verb": "sentir.2",
            "comment": "Lamentar algo que ha ocurrido, preferir 
                       que no hubiera ocurrido",
            "roles": {
                "arg0": "Persona que lamenta",
                "arg1": "Evento ocurrido"
            }
        }
    ]
}
```
## Framesets

```json
{
  "id": "111",
  "verb": "vestir.1",
  "comment": "Poner o llevar puesta [ropa]",
  "roles": {
      "arg0": "Persona que viste",
      "arg1": "Persona usando ropa",
      "arg2": "Ropa"
  }
}
```

### Creating a new frameset
The user will be prompted with AnCora verb list. Once the desired verb is selected, the ADESSE verb senses will be updated and will be found in the dropdown menu of 'Verb sense description'. The user must then specify the arguments of the frameset.

## ADESSE Handler
To facilitate annotation/creation of framesets we include an ADESSE handler that
obtains the verb senses and verb definitions listed on the database. When creating
a frameset a user will be prompted with the verb senses listed on ADESSE and can
additionally create a new one if the one(s) listed do not match the sentence context.

Reflexive verbs are expressed differently in ADESSE than in PropBank.
PropBank considers: to dress and to dress oneself as two different verb
senses for the verb lemma 'dress'. In terms of argument structure,
PropBank marks arg0 as the 'person that dresses', arg1 as the 'person using clothes', and arg2 as 'clothes' to the sense 'to dress'. For the sense 'to dress oneself' it marks arg0 and arg1 as the same argument. Meaning that the roleset for that verb sense is: arg0 and arg1 only. ADDESSE keeps the arg1 and simply marks it as REFL. For the sake of consistency with PropBank, annotations should follow PropBank's guidelines. ADESSE will be used only as a reference guide for verb sense description, not argument structure. 

Eventually, the goal will be to present the ADESSE entry for the verb alongside the annotated version of PropBank. To have the information of both resources in a single verb instance page. As the English PropBank counterpart does with FrameNet and VerbNet.