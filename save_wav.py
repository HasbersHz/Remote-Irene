def saywav_to_file(saywav_result,wavfile):
    b64 = saywav_result["wav_base64"]
    base64_message = b64.encode('utf-8')

    import base64

    with open(wavfile, 'wb') as file:
        file.write(base64.decodebytes(base64_message))
