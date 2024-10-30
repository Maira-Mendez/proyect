import requests

# Clave API y URLs base
api_key = "abb6ca15b78158785a3a2a54a45170a7"
base_url = "https://api.themoviedb.org/3"
base_image_url = "https://image.tmdb.org/t/p/"

# Función para buscar la película por nombre y obtener el póster
def obtener_imagen_por_nombre(nombre_pelicula, tamaño="w500"):
    # Endpoint de búsqueda de película
    url_busqueda = f"{base_url}/search/movie"
    params_busqueda = {
        "api_key": api_key,
        "query": nombre_pelicula,
        "language": "es-ES"
    }
    
    # Hacemos la búsqueda de la película
    response_busqueda = requests.get(url_busqueda, params=params_busqueda)
    if response_busqueda.status_code == 200:
        resultados = response_busqueda.json().get("results")
        if resultados:
            # Selecciona la primera película que coincide en los resultados
            pelicula = resultados[0]
            poster_path = pelicula.get("poster_path")
            if poster_path:
                # Construimos la URL completa de la imagen
                imagen_url = f"{base_image_url}{tamaño}{poster_path}"
                return imagen_url
            else:
                print("No se encontró el póster para esta película.")
                return None
        else:
            print("No se encontraron resultados para esta búsqueda.")
            return None
    else:
        print("Error al buscar la película:", response_busqueda.status_code)
        return None

# Ejemplo de uso
imagen_url = obtener_imagen_por_nombre("Moana")  # Usando el nombre de la película
if imagen_url:
    print("URL de la imagen:", imagen_url)