# Roy Basmacier 24813
# Samuel Lee 24774
import random
import DS


def gen_random_tx(q, p, g):
  tx = '*** Bitcoin transaction ***\n'
  serial_number = random.randint(0, pow(2,128)-1)
  tx += 'Serial number: ' + str(serial_number) + '\n'
  payer_alpha, payer_beta = DS.KeyGen(q, p, g) # get from ds.py
  tx += 'Payer public key (beta): ' + str(payer_beta) + '\n'
  payee_alpha, payee_beta = DS.KeyGen(q, p, g) # get from ds.py
  tx += 'Payee public key (beta): ' + str(payee_beta) + '\n'
  amount = random.randint(1, pow(10,6))
  tx += 'Amount: ' + str(amount) + '\n'
  s, r = DS.SignGen(tx.encode('UTF-8'), q, p, g, payer_alpha) # get from ds.py
  tx += 'Signature (s): ' + str(s) + '\n'
  tx += 'Signature (r): ' + str(r)
  # print(tx)
  return tx
