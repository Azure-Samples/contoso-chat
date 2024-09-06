import json
import prompty
# to use the azure invoker make 
# sure to install prompty like this:
# pip install prompty[azure]
import prompty.azure
from prompty.tracer import trace, Tracer, console_tracer, PromptyTracer
from dotenv import load_dotenv
load_dotenv()
import os

# add console and json tracer:
# this only has to be done once
# at application startup
Tracer.add("console", console_tracer)
json_tracer = PromptyTracer()
Tracer.add("PromptyTracer", json_tracer.tracer)

@trace
def fluency_evaluation(    
      question: any,
      context: any,
      answer: any
) -> str:

  # execute the prompty file
  model_config = {
        "azure_endpoint": os.environ["AZURE_OPENAI_ENDPOINT"],
        "api_version": os.environ["AZURE_OPENAI_API_VERSION"],
  }
  result = prompty.execute(
    "fluency.prompty", 
    inputs={
      "question": question,
      "context": context,
      "answer": answer
    },
    configuration=model_config
  )

  return result

if __name__ == "__main__":
   json_input = '''{
  "question": "What feeds all the fixtures in low voltage tracks instead of each light having a line-to-low voltage transformer?",
  "context": "Track lighting, invented by Lightolier, was popular at one period of time because it was much easier to install than recessed lighting, and individual fixtures are decorative and can be easily aimed at a wall. It has regained some popularity recently in low-voltage tracks, which often look nothing like their predecessors because they do not have the safety issues that line-voltage systems have, and are therefore less bulky and more ornamental in themselves. A master transformer feeds all of the fixtures on the track or rod with 12 or 24 volts, instead of each light fixture having its own line-to-low voltage transformer. There are traditional spots and floods, as well as other small hanging fixtures. A modified version of this is cable lighting, where lights are hung from or clipped to bare metal cables under tension",
  "answer": "The main transformer is the object that feeds all the fixtures in low voltage tracks."
}'''
   args = json.loads(json_input)

   result = fluency_evaluation(**args)
   print(result)
