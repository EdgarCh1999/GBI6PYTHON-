def enzima(seq, site):
    # Sitios de empalme de las enzimas EcoR1, HindIII y NotI
    enzymes = {
        "EcoR1": "GAATTC",
        "HindIII": "AAGCTT",
        "NotI": "GCGGCCGC"
    }
    
    # Verificar que el sitio de empalme especificado es válido
    if site not in enzymes.values():
        print(f"Error: El sitio de empalme {site} no corresponde a ninguna de las enzimas definidas.")
        return []
    
    # Inicializar la lista de fragmentos resultantes
    fragments = []
    
    # Dividir la secuencia en fragmentos en cada sitio de corte
    while True:
        # Buscar el siguiente sitio de corte en la secuencia
        sitiocorte = seq.find(site)
        
        # Si no se encuentra más sitios de corte, agregar el fragmento restante y salir del bucle
        if sitiocorte == -1:
            fragments.append([seq, len(seq)])
            break
        
        # Dividir la secuencia en el sitio de corte y agregar el fragmento resultante a la lista
        frag = seq[:sitiocorte + len(site)]
        fragments.append([frag, len(frag)])
        
        # Actualizar la secuencia para buscar el siguiente sitio de corte
        seq = seq[sitiocorte + len(site):]
    
    # Devolver la lista con los fragmentos resultantes y sus longitudes
    return(fragments)





