from itertools import chain
import csv

reader = csv.reader(open("store_ready.csv", "r"), delimiter=',')
writer = csv.writer(open("store_ready_semi.csv", 'w'), delimiter=';')
writer.writerows(reader)


def split_file(filename, pattern, size):
    """Split a file into multiple output files.

    The first line read from 'filename' is a header line that is copied to
    every output file. The remaining lines are split into blocks of at
    least 'size' characters and written to output files whose names
    are pattern.format(1), pattern.format(2), and so on. The last
    output file may be short.

    """



#    with open("store_ready_semi.csv", 'rb') as f:
 #       header = next(f)
  #      for index, line in enumerate(f, start=1):
   #         with open(pattern.format(index), 'wb') as out:
    #            out.write(header)
     #           n = 0
      #          for line in chain([line], f):
       #             out.write(line)
        #            n += len(line)
         #           if n >= size:
          #              break

#if __name__ == '__main__':
 #   split_file('data.csv', '{0:04d} store info.csv', 1)
 
