import csv
from django.core.management.base import BaseCommand
from bolsa.models import Tipo_trx
#para ejecutarlo, es en la terminal python manage.py load_tipotrxs

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        archivo = open("data/tipotrx.csv", "r")
        # archivo = open("../proyecto_inmuebles/data/ciudades.csv", "r") para linux
        reader = csv.reader(archivo, delimiter=";")
        next(reader)  # Se salta la primera linea

        for numero_fila, fila in enumerate(reader, start=2):
            try:
                if len(fila) < 2:  # Asegúrate de que haya suficientes datos en cada fila
                    self.stdout.write(
                        self.style.WARNING(
                            f"Fila {numero_fila}: Datos incompletos, se omite: {fila}"
                        )
                    )
                    continue


                # Crear el curso
                Tipo_trx.objects.create(
                    id_tipo=fila[0],
                    tipotrx=fila[1]                )

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Error en fila {numero_fila}: {str(e)}")
                )

        archivo.close()
