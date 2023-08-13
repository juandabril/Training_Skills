def escribir(fpath,data_in):
    """
    summary for escribir
    Args:
        fpath ([type]): path absoluto
        data_in ([type]): información a escribir
    """
    with open (fpath,'w') as file_:
        file_.write(data_in)

    #assert algo