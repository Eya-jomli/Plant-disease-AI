import os
import json
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from plant_disease.Model.typePlant import TypePlante

# Set up logging
logger = logging.getLogger(__name__)

# Set up the Google API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Check if the API key is set
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    logger.info("Google API key successfully configured.")
else:
    logger.error("Google API key is not set.")

def ai_generate_description(nom):
    """Generate a detailed description for a plant name using the AI model."""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Generate a detailed description in 4 lines for: {nom}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        logger.error("Error in AI model generation: %s", str(e))
        return "Error generating description."

@csrf_exempt
def generate_description(request):
    """View to generate a description for a given plant name."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nom = data.get('nom', '')
            if not nom:
                logger.error("No name provided for description generation.")
                return JsonResponse({'error': 'No name provided.'}, status=400)
            
            description = ai_generate_description(nom)
            return JsonResponse({'description': description})
        except json.JSONDecodeError:
            logger.error("Error decoding JSON request body.")
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            logger.error("Error generating description: %s", str(e))
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid Request'}, status=400)

# List views for TypePlante
class TypePlanteListView(ListView):
    model = TypePlante
    template_name = 'type_plante/typeplante_list.html'
    context_object_name = 'plantes'

class TypePlanteListViewFront(ListView):
    model = TypePlante
    template_name = 'type_plante/indexFront.html'
    context_object_name = 'plantes'
    
class TypePlanteDetailView(DetailView):
    model = TypePlante
    template_name = 'type_plante/typeplante_detail.html'
    context_object_name = 'plante'

class TypePlanteCreateView(CreateView):
    model = TypePlante
    fields = ['nom', 'description', 'image']
    template_name = 'type_plante/typeplante_form.html'
    success_url = '/typePlantes/'

class TypePlanteUpdateView(UpdateView):
    model = TypePlante
    fields = ['nom', 'description', 'image']
    template_name = 'type_plante/typeplante_form.html'
    success_url = '/typePlantes/'

class TypePlanteDeleteView(DeleteView):
    model = TypePlante
    template_name = 'type_plante/typeplante_confirm_delete.html'
    success_url = '/typePlantes/'
