## Load environment variables
from dotenv import load_dotenv
load_dotenv()

import json
import prompty
# to use the azure invoker make 
# sure to install prompty like this:
# pip install prompty[azure]
import prompty.azure
from prompty.tracer import trace, Tracer, console_tracer, PromptyTracer

# add console and json tracer:
# this only has to be done once
# at application startup
Tracer.add("console", console_tracer)
json_tracer = PromptyTracer()
Tracer.add("PromptyTracer", json_tracer.tracer)

# if your prompty file uses environment variables make
# sure they are loaded properly for correct execution

@trace
def run(    
      customer: any,
      documentation: any,
      question: any
) -> str:

  # execute the prompty file
  result = prompty.execute(
    "chat-3.prompty", 
    inputs={
      "customer": customer,
      "documentation": documentation,
      "question": question
    }
  )

  return result

if __name__ == "__main__":
   json_input = '''{
  "customer": {
    "id": "1",
    "firstName": "John",
    "lastName": "Smith",
    "age": 35,
    "membership": "Base",
    "orders": [
      {
        "id": 29,
        "productId": 8,
        "name": "Alpine Explorer Tent",
        "description": "Welcome to the joy of camping with the Alpine Explorer Tent! This robust, 8-person, 3-season marvel is from the responsible hands of the AlpineGear brand. Promising an enviable setup that is as straightforward as counting sheep, your camping experience is transformed into a breezy pastime. Looking for privacy? The detachable divider provides separate spaces at a moment's notice. Love a tent that breathes? The numerous mesh windows and adjustable vents fend off any condensation dragon trying to dampen your adventure fun. The waterproof assurance keeps you worry-free during unexpected rain dances. With a built-in gear loft to stash away your outdoor essentials, the Alpine Explorer Tent emerges as a smooth balance of privacy, comfort, and convenience. Simply put, this tent isn't just a shelter - it's your second home in the heart of nature! Whether you're a seasoned camper or a nature-loving novice, this tent makes exploring the outdoors a joyous journey."
      }
    ]
  },
  "documentation": {
    "id": "1",
    "title": "Alpine Explorer Tent",
    "name": "Alpine Explorer Tent",
    "content": "Welcome to the joy of camping with the Alpine Explorer Tent! This robust, 8-person, 3-season marvel is from the responsible hands of the AlpineGear brand. Promising an enviable setup that is as straightforward as counting sheep, your camping experience is transformed into a breezy pastime. Looking for privacy? The detachable divider provides separate spaces at a moment's notice. Love a tent that breathes? The numerous mesh windows and adjustable vents fend off any condensation dragon trying to dampen your adventure fun. The waterproof assurance keeps you worry-free during unexpected rain dances. With a built-in gear loft to stash away your outdoor essentials, the Alpine Explorer Tent emerges as a smooth balance of privacy, comfort, and convenience. Simply put, this tent isn't just a shelter - it's your second home in the heart of nature! Whether you're a seasoned camper or a nature-loving novice, this tent makes exploring the outdoors a joyous journey.",
    "description": "Welcome to the joy of camping with the Alpine Explorer Tent! This robust, 8-person, 3-season marvel is from the responsible hands of the AlpineGear brand. Promising an enviable setup that is as straightforward as counting sheep, your camping experience is transformed into a breezy pastime. Looking for privacy? The detachable divider provides separate spaces at a moment's notice. Love a tent that breathes? The numerous mesh windows and adjustable vents fend off any condensation dragon trying to dampen your adventure fun. The waterproof assurance keeps you worry-free during unexpected rain dances. With a built-in gear loft to stash away your outdoor essentials, the Alpine Explorer Tent emerges as a smooth balance of privacy, comfort, and convenience. Simply put, this tent isn't just a shelter - it's your second home in the heart of nature! Whether you're a seasoned camper or a nature-loving novice, this tent makes exploring the outdoors a joyous journey."
  },
  "question": "What cold-weather sleeping bag would go well with what I have already purchased?"
}'''
   args = json.loads(json_input)

   result = run(**args)
   print(result)
