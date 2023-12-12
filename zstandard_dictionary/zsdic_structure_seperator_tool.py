import struct
import os
import time

appVer = "3"

def extract_dictionary_parts(dictionary_file_path, output_dir):
    with open(dictionary_file_path, 'rb') as file:
        # Read and parse the header
        header_data = file.read(8)  # Adjust the size based on the actual header structure
        with open(os.path.join(output_dir, 'header.txt'), 'wb') as header_file:
            header_file.write(header_data)

        # Read and parse the literals section
        literals_size = struct.unpack('<Q', file.read(8))[0]
        literals_data = file.read(literals_size)
        with open(os.path.join(output_dir, 'literals.txt'), 'wb') as literals_file:
            literals_file.write(literals_data)

        # Read and parse the symbol frequencies
        frequencies_size = struct.unpack('<Q', file.read(8))[0]
        frequencies_data = file.read(frequencies_size)
        with open(os.path.join(output_dir, 'frequencies.txt'), 'wb') as frequencies_file:
            frequencies_file.write(frequencies_data)

        # Read and parse the variable-length code assignments
        codes_size = struct.unpack('<Q', file.read(8))[0]
        codes_data = file.read(codes_size)
        with open(os.path.join(output_dir, 'codes.txt'), 'wb') as codes_file:
            codes_file.write(codes_data)

        # Read and parse other sections as needed...

if __name__ == "__main__":
    print("zsdic_structure_seperator_tool\nVersion: " + appVer)
    os.makedirs(os.path.join("zsdic", "zs"))
    os.makedirs(os.path.join("zsdic", "pack"))
    os.makedirs(os.path.join("zsdic", "bcett_byml"))
    for Tuple in [('zs.zsdic', os.path.join("zsdic", "zs")), 
                  ('pack.zsdic', os.path.join("zsdic", "pack")),
                  ('bcett.byml.zsdic', os.path.join("zsdic", "bcett_byml"))]:
        extract_dictionary_parts(Tuple[0], Tuple[1])
    print("Done!")
    time.sleep(5)