'''
Created on 08/02/2018

@author: Utilizador
'''


from Bio import SeqIO



if __name__ == '__main__':

    file_name = 'ref_H3.fasta'
    max_size = 1000
    
    with open(file_name, 'r') as handle_in:
        with open('ref_H3_{}.fasta'.format(max_size), 'w') as handle_out:
            lst_seq_record = []
            for seq_record in SeqIO.parse(handle_in, 'fasta'):
                print(seq_record.id, len(str(seq_record.seq)))
                if (len(str(seq_record.seq)) < max_size):
                    print('>{} {}\n{}\n'.format(seq_record.id, len(str(seq_record.seq)), str(seq_record.seq)))
                    seq_record.seq.description = 'len: {}'.format(len(str(seq_record.seq)))
                    lst_seq_record.append(seq_record)
        if (len(lst_seq_record) > 0):
            with open('ref_H3.fasta'.format(max_size), 'w') as handle_out:
                            
                ## save_sequences
                SeqIO.write(lst_seq_record, handle_out, 'fasta')
            
    print('finish')
    
    pass