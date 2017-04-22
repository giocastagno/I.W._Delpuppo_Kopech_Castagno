    #calificacion itinerario
    MALO = '1'
    MEDIOCRE = '2'
    BUENO = '3'
    MUY_BUENO = '4'
    EXCELENTE = '5'
    calificaciones = (
        (MALO, 'Malo'),
        (MEDIOCRE, 'Regular'),
        (BUENO, 'Bueno'),
        (MUY_BUENO, 'Muy bueno'),
        (EXCELENTE, 'Excelente'),
    )
    calificacion_general = models.CharField(max_length = 2, choices=calificaciones, default=BUENO)