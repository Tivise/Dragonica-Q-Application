from tkinter import *

fenetre = Tk()
fenetre.title("Quest Generator")
fenetre.minsize(width=600, height=800)
""" Déclaration des fenêtres:"""
Sfenetre_global = Frame(fenetre, borderwidth=2, relief=GROOVE)
Sfenetre_global.grid(row=0, column=0, ipadx=30)
Sfenetre_parler = Frame(fenetre, borderwidth=2, relief=GROOVE)
Sfenetre_parler.grid(row=1, column=0, ipadx=30)

""" Contenu de la Fenêtre Global:"""
titrePrincipal = Label(Sfenetre_global, text='Quest Generator (by Tivise)', fg='red').grid(row=0,column=2)
separator = Label(Sfenetre_global,text='').grid(row=1,column=0)
globaltitle_label = Label(Sfenetre_global, font=("Arial Bold", 15), text='Global').grid(row=2,column=2)
separator2 = Label(Sfenetre_global,text='').grid(row=3,column=0)
questID_label = Label(Sfenetre_global, text='Quest ID').grid(row=4,column=0)
questID_content = IntVar()
questID_form = Entry(Sfenetre_global, textvariable=questID_content)
questID_form.grid(row=4,column=1)
questID_form.focus_set()

groupquestID_label = Label(Sfenetre_global, text='GroupQuest ID').grid(row=4,column=2)
groupquestID_content = IntVar()
groupquestID_form = Entry(Sfenetre_global, textvariable=groupquestID_content)
groupquestID_form.grid(row=4,column=3)
groupquestID_form.focus_set()

separator3 = Label(Sfenetre_global,text='').grid(row=5,column=0)

questName_label = Label(Sfenetre_global, text='Quest Name').grid(row=6,column=0)
questName_content = StringVar()
questName_form = Entry(Sfenetre_global, textvariable=questName_content, width=75)
questName_form.grid(row=6,column=1, columnspan=5)
questName_form.focus_set()

npcName_label = Label(Sfenetre_global, text='NPC GUID').grid(row=7,column=0)
npcName_content = StringVar()
npcName_form = Entry(Sfenetre_global, textvariable=npcName_content, width=30)
npcName_form.grid(row=7,column=1)
npcName_form.focus_set()
npcFace_label = Label(Sfenetre_global, text='NPC_FACE').grid(row=7,column=2)
npcFace_content = StringVar()
npcFace_form = Entry(Sfenetre_global, textvariable=npcFace_content, width=20)
npcFace_form.grid(row=7,column=3)
npcFace_form.focus_set()

separator4 = Label(Sfenetre_global,text='').grid(row=8,column=0)
globalselection_label = Label(Sfenetre_global, font=("Arial Bold", 15), text='Event Selection').grid(row=9,column=2)

btn_parler = Button(Sfenetre_global, text="Talk Event").grid(row=10, column=0)


"""Contenu de la Fenêtre Parler:"""
separator5 = Label(Sfenetre_parler,text='').grid(row=11,column=0)
npcNameEnd_label = Label(Sfenetre_parler, text='Talk to who? GUID').grid(row=12,column=0)
npcNameEnd_content = StringVar()
npcNameEnd_form = Entry(Sfenetre_parler, textvariable=npcNameEnd_content, width=30)
npcNameEnd_form.grid(row=12,column=1)
npcNameEnd_form.focus_set()
npcFaceEnd_label = Label(Sfenetre_parler, text='FACE').grid(row=12,column=2)
npcFaceEnd_content = StringVar()
npcFaceEnd_form = Entry(Sfenetre_parler, textvariable=npcFaceEnd_content, width=20)
npcFaceEnd_form.grid(row=12,column=3)
npcFaceEnd_form.focus_set()

separator6 = Label(Sfenetre_parler,text='').grid(row=13,column=0)
talkEvent_msg_label = Label(Sfenetre_parler, text='Event message').grid(row=14,column=0)
talkEvent_msg_content = StringVar()
talkEvent_msg_form = Entry(Sfenetre_parler, textvariable=talkEvent_msg_content, width=50)
talkEvent_msg_form.grid(row=14,column=1, columnspan=3)
talkEvent_msg_form.focus_set()

separator7 = Label(Sfenetre_parler,text='').grid(row=15,column=0)

talk_msg_intro_label = Label(Sfenetre_parler, text='Intro message').grid(row=16,column=0)
talk_msg_intro_content = StringVar()
talk_msg_intro_form = Entry(Sfenetre_parler, textvariable=talk_msg_intro_content, width=75)
talk_msg_intro_form.grid(row=16,column=1, columnspan=5)
talk_msg_intro_form.focus_set()

separator8 = Label(Sfenetre_parler,text='').grid(row=17,column=0)

talk_msg_accept_label = Label(Sfenetre_parler, text='Accept message').grid(row=18,column=0)
talk_msg_accept_content = StringVar()
talk_msg_accept_form = Entry(Sfenetre_parler, textvariable=talk_msg_accept_content, width=75)
talk_msg_accept_form.grid(row=18,column=1, columnspan=5)
talk_msg_accept_form.focus_set()

separator9 = Label(Sfenetre_parler,text='').grid(row=19,column=0)

talk_msg_attente_label = Label(Sfenetre_parler, text='Waiting message').grid(row=20,column=0)
talk_msg_attente_content = StringVar()
talk_msg_attente_form = Entry(Sfenetre_parler, textvariable=talk_msg_attente_content, width=75)
talk_msg_attente_form.grid(row=20,column=1, columnspan=5)
talk_msg_attente_form.focus_set()

separator10 = Label(Sfenetre_parler,text='').grid(row=21,column=0)

talk_msg_confirm_label = Label(Sfenetre_parler, text='Confirm message').grid(row=22,column=0)
talk_msg_confirm_content = StringVar()
talk_msg_confirm_form = Entry(Sfenetre_parler, textvariable=talk_msg_confirm_content, width=75)
talk_msg_confirm_form.grid(row=22,column=1, columnspan=5)
talk_msg_confirm_form.focus_set()

separator11 = Label(Sfenetre_parler,text='').grid(row=23,column=0)

talk_msg_objectif_label = Label(Sfenetre_parler, text='Objectif').grid(row=24,column=0)
talk_msg_objectif_content = StringVar()
talk_msg_objectif_form = Entry(Sfenetre_parler, textvariable=talk_msg_objectif_content, width=75)
talk_msg_objectif_form.grid(row=24,column=1, columnspan=5)
talk_msg_objectif_form.focus_set()
talk_msg_validation_label = Label(Sfenetre_parler, text='NPC validation').grid(row=25,column=0)
talk_msg_validation_content = StringVar()
talk_msg_validation_form = Entry(Sfenetre_parler, textvariable=talk_msg_validation_content, width=75)
talk_msg_validation_form.grid(row=25,column=1, columnspan=5)
talk_msg_validation_form.focus_set()
talk_msg_additionnal_label = Label(Sfenetre_parler, text='Additional info.').grid(row=26,column=0)
talk_msg_additionnal_content = StringVar()
talk_msg_additionnal_form = Entry(Sfenetre_parler, textvariable=talk_msg_additionnal_content, width=75)
talk_msg_additionnal_form.grid(row=26,column=1, columnspan=5)
talk_msg_additionnal_form.focus_set()

def sendquest():
    tableau = {
        'quest_name_id': 960000,
        'quest_eventmsg_id': 970000,
        'quest_intromsg_id': 980000,
        'quest_acceptmsg': 990000,
        'quest_attentemsg': 110000,
        'quest_confirmmsg': 120000,
        'quest_bloc_id': 130000
    }
    for key, value in tableau.items():
        tableau[key] = value + int(questID_content.get()) - 4000
    fichier = open('QUEST' + str(questID_content.get()) + '.xml', "a", encoding='utf-8')
    fichier.write('<?xml version="1.0" encoding="euc-kr"?>'
    '\n <!-- Quest Generator by PAZDER Thomas(Tivise) -->\n'
    f' <QUEST>\n <ID>{questID_content.get()}</ID>\n'
    f'<GROUPNO>0</GROUPNO> \n <TITLE TEXT="{tableau["quest_name_id"]}"></TITLE>\n'
    f'<GROUPNAME TEXT="{groupquestID_content.get()}"></GROUPNAME>\n'
    f'	<CLIENTS>\n<CLIENT TYPE="NPC" EVENTNO="10000">{npcName_content.get()}</CLIENT>\n'
    f'</CLIENTS>\n <AGENTS> \n <AGENT TYPE="NPC" EVENTNO="10001">{npcName_content.get()}</AGENT>\n'
    f'<AGENT TYPE="NPC" EVENTNO="10002" MARK="END">{npcNameEnd_content.get()}</AGENT>\n </AGENTS>\n <PAYERS>\n'
    f'<PAYER TYPE="NPC" EVENTNO="10003">{npcNameEnd_content.get()}</PAYER>\n </PAYERS>\n'
    '<EVENTS>\n <NPC OBJECTNO="0" TYPE="CLIENT" VALUE="101">10000</NPC>\n<NPC OBJECTNO="0" TYPE="ING_DLG" VALUE="501">10001</NPC>\n'
    '<NPC OBJECTNO="0" TYPE="ING_DLG" VALUE="601">10002</NPC>\n<NPC OBJECTNO="1" TYPE="INCPARAM" VALUE="601/1">10002</NPC>\n'
    '<NPC OBJECTNO="0" TYPE="PAYER" VALUE="601">10003</NPC>\n</EVENTS>\n'
    f'<OBJECTS TYPE="NOSTEP">\n<OBJECT1 COUNT="1" TEXT="{tableau["quest_eventmsg_id"]}"/>\n</OBJECTS>\n'
    f'<DIALOGS>\n<DIALOG ID="101" TYPE="PROLOG">\n<BODY TEXT="{talk_dialogue_debut_id}" FACE="{talk_deb_face}"/>\n<SELECT ID="10000" TYPE="ACCEPT" TEXT="500004"></SELECT>\n</DIALOG>\n'
    f'<DIALOG ID="301">\n<BODY TEXT="{talk_dialogue_accept_id}" FACE="{talk_deb_face}"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
    f'<DIALOG ID="501">\n<BODY TEXT="{talk_dialogue_encours_id}" FACE="{talk_deb_face}"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
    f'<DIALOG ID="552">\n<BODY TEXT="{talk_dialogue_confirm_id}" FACE="{talk_end_face}"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
    f'<DIALOG ID="601" TYPE="COMPLETE">\n<BODY TEXT="{talk_dialogue_confirm_id}" FACE="{talk_end_face}"/>\n<SELECT ID="30999" TYPE="COMPLETE" TEXT="500007"></SELECT>\n</DIALOG>\n'
    '<DIALOG ID="701">\n<BODY TEXT="500017"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
    '<DIALOG ID="801">\n<BODY TEXT="500018"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
    f'<DIALOG ID="901" TYPE="INFO">\n<BODY TEXT="{talk_questinfo_id}"/>\n</DIALOG>\n'
    '<DIALOG ID="902">\n<BODY TEXT="502048"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
    '<DIALOG ID="903">\n<BODY TEXT="501835"/>\n<SELECT ID="0" TEXT="500003"></SELECT>\n</DIALOG>\n'
    '</DIALOGS>\n</QUEST>'

)











btn_send = Button(fenetre, text="Send", command=sendquest).grid(row=3, column=0)


fenetre.mainloop()