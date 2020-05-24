#odoo
Convenciones para el desarrollo de módulos en Odoo:
- Los nombre de los módulos deben ser asignados de la siguiente forma "codigoproyecto_nombremodulo".
- La estructura de los módulos de ahora en adelante será la siguiente:
	* exp_modulo_example
		* models (Archivos Python)
		* i18n  (Traducciones)
		* views (contiene las vistas y menus en archivos xml)
		* controllers (Solo necesario si modifican rutas del Framework WCGI Werzburg ó es un módulo Frontend)
		* security (Carpeta obligatoría sino se definen solo el administrador podra ver los modelos creados)
		* demo (Contendrá data demo para los test)
		* data (Contendrá la data por defecto que cargará el módulo para su operación)
		* test (Todo módulo debe contener sus Unittest)
		* docs (Carpeta donde se generá la documentación a partir de docstring usando sphinx)
		* wizards (Contendrá todos los asistentes desarrollados para el módulo)
			* views (Contendrá las vistas xml del asistente)
			* models (Archivos Python del asistente)
- Cada función y código deberán contener su respectivo docstring al momento de terminar la función siguiendo
se debe seguir el siguiente estilo http://www.sphinx-doc.org/es/stable/ext/example_google.html#example-google.
- Antes de proponer merge se deben realizar las pruebas ATDD de flujo del módulo y grabarlas para adjuntarlas con
la propuesta de merge.
- Evitar el código repetitivo, si es necesario usar el mismo código varias veces crear una función para esto.
- Las funciones no podrán contener más de 10 condiciones en su lógica, sino es posible reducirlas se deberá aplicar la regla
"Divide y venceras".
- Antes de proponer merge probar que los Unittest estén funcionando correctamente.
- No se hará merge de código que no cumpla con las pautas establecidas.
- Las ramas de los Fix urgentes para proyectos serán nombrados con la siguiente convención HOTFIX-FechaDelFix-Número(001-999), por ejemplo
si hoy 31/01/2018 hay un fix urgente se nombrará el branch de la siguiente manera usuariogit/CON/HOTFIX-20180131-001, si mañana se realiza otro fix,
sería usuariogit/CON/HOTFIX-20180201-001.
- Todo hotfix debe ser verificado mediante Unittest y Pruebas ATDD, y un video del flujo debe ser adjuntado a la propuesta de merge.
- No se relizarán merge de Hotfix que no hayan sido probados o que no cumplan con el punto anterior.
- La historía de lo commits deben ser descriptivas, se utilizaran las siguientes etiquetas:
	* IMP - Improvement: Se aplicá a mejoras y nuevas funcionalidades.
	* UPD - Update: Se aplicá cuando se actualizan archivos de data, vistas y data demo.
	* FIX - Fix: Se aplicá cuando se realiza un fix al código.
	* DEL - Delete: Se aplicá cuando se ha borrado un archivo, linea de código o carpeta.
	* ADD - Adds: Se aplicá cuando se ha agregado un nuevo archivo o carpeta.
- Si dentro del código fuente se encuentram secciones o lineas a mejorar se procederá a dejar un label TODO con la descripción, por ejemplo:
	# ~ TODO: Please change the name of the variable for a more descriptive name.
	sdf = dict(str, int)
