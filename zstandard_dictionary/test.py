import sarc

fp = r"C:\Users\ecrje\PycharmProjects\Totk-Modding-Tools-and-Research\zstandard_dictionary\raw\ZsDic.pack"
out_dir = r"C:\Users\ecrje\PycharmProjects\Totk-Modding-Tools-and-Research\zstandard_dictionary\raw\pack_extraction"

with open(fp, 'rb') as f:
    sarc_controller = sarc.read_file_and_make_sarc(f)

sarc_controller.extract_to_dir(out_dir)
