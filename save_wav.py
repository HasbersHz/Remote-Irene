def saywav_to_file(saywav_result,wavfile):
    import base64

    base64_message = saywav_result["wav_base64"].encode('utf-8')

    with open(wavfile, 'wb') as file:
        file.write(base64.decodebytes(base64_message))
