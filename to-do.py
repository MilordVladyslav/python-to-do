import json 
from random import randrange

def readToDoFile():
  try:
    toDoList = json.load(open("to-do-list.json"))
  except:
    toDoList = []
  return toDoList

toDoList = readToDoFile()

def isExistedNote(noteValue = '', toDoList = []):
  return noteValue not in [value.get("value") for value in toDoList]

def createNote(noteValue = ''):

  if (noteValue):
    if isExistedNote(noteValue, toDoList):
      newNote = {
        "value": noteValue,
        "isCompleted": False
      }

      toDoList.append(newNote)
      with open("to-do-list.json", "w") as file:
        json.dump(toDoList, file, indent=2, ensure_ascii=False)
      return newNote
    else:
      print('You already have this note')
  else:
    print('Empty sting is invalid value, please, fill the input')
    return False

# possible state : 'allNotes', 'completedNotes', 'uncompletedNotes'
def readNotes(state = ''):
  if state == 'allNotes':
    if len(toDoList):
      for note in toDoList: 
        isCompleted = 'completed!' if note.get('isCompleted') else 'not completed!'
        print(note.get("value") + " - " + isCompleted )
    else:
      print('you do not have notes!')
  elif state == 'completedNotes':
    filteredResult = filterNotes(True)
    if len(filteredResult):
      for note in filteredResult:
        print(note.get("value") + " - " + 'completed')
    else:
      print('you do not have completed notes!')
  elif state == 'uncompletedNotes':
    filteredResult = filterNotes(False)
    if len(filteredResult):
      for note in filteredResult:
        print(note.get("value") + " - " + 'not completed')
    else:
      print('you do not have uncompleted notes!')

def filterNotes(isCompleted):
  return [completed for completed in toDoList if completed['isCompleted'] == isCompleted]
  
def changeNoteValue(noteCurrentValue = '', noteNewValue = ''):
  index = next((i for i, item in enumerate(toDoList) if item['value'] == noteCurrentValue), -1)
  if index > -1 :
    if toDoList[index]['value'] != noteNewValue:
      toDoList[index]['value'] = noteNewValue
      with open("to-do-list.json", "w") as file:
        json.dump(toDoList, file, indent=2, ensure_ascii=False)    
  else:
    print('this element does not exist!')

def changeNoteStatus(noteCurrentValue = '', noteNewStatus = 0):
  index = next((i for i, item in enumerate(toDoList) if item['value'] == noteCurrentValue), -1)
  if index > -1 :
    noteNewStatus = True if noteNewStatus == '1' else False
    if toDoList[index]['isCompleted'] != noteNewStatus:
      toDoList[index]['isCompleted'] = noteNewStatus
      with open("to-do-list.json", "w") as file:
        json.dump(toDoList, file, indent=2, ensure_ascii=False)    
  else:
    print('this element does not exist!')

def deleteNote(noteCurrentValue):
  index = next((i for i, item in enumerate(toDoList) if item['value'] == noteCurrentValue), -1)
  if index > -1:
    toDoList.pop(index)
    with open("to-do-list.json", "w") as file:
      json.dump(toDoList, file, indent=2, ensure_ascii=False)   
  else:
    print('this element does not exist!')

def keyboardInterruptHandling(text = ''):
  try:
    action = input(text)
  except:
    print('\n')
    exit()
  return action
  
def gameManager():
  availableCommands = ['createNote', 'readCompletedNotes', 'readUncompletedNotes', 'readAllNotes', 'changeNoteValue', "changeNoteStatus", 'deleteNote']
  print(' ')
  try:
    action = keyboardInterruptHandling('Welcome to the to-do list, please, type LIST for the available actions or write your action: ')
  except:
    print('\n')
    exit()
  print(' ')
  if action == 'LIST':
    for command in availableCommands:
      print(command)
  elif action == 'createNote' :
    createNoteValue = keyboardInterruptHandling('please name your note: ')
    createNote(createNoteValue)
  elif action == 'readCompletedNotes':
    readNotes('completedNotes')
  elif action == 'readUncompletedNotes':
    readNotes('uncompletedNotes')
  elif action == 'readAllNotes':
    readNotes('allNotes')
  elif action == 'changeNoteValue':
    currentNoteValue = keyboardInterruptHandling('please select a value of the note: ')
    if currentNoteValue: 
      newValue = keyboardInterruptHandling('please select a new value for the note: ')
      if newValue:
        changeNoteValue(currentNoteValue, newValue)
      else:
        print('incorrect value!')
    else:
      print('incorrect value!')
  elif action == 'changeNoteStatus':
    currentNoteValue = keyboardInterruptHandling('please select a value of the note: ')
    if currentNoteValue:
      status = keyboardInterruptHandling('choose 1 if you wanna put the note into completed list or any other key if you wanna put the note into uncompleted list: ')
      changeNoteStatus(currentNoteValue, status)
    else:
      print('incorrect value!')
  elif action == 'deleteNote':
    currentNoteValue = keyboardInterruptHandling('please select a value of the note: ')
    if currentNoteValue:
      deleteNote(currentNoteValue)
    else:
      print('incorrect value!')

  gameManager()

gameManager()
