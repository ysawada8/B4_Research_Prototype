import glob
import os
import subprocess
from my_module import skip_line_and_return_as_str
import codecs
import re
from my_module import seg_token_diff
from natsort import natsorted
from my_module import test_cand
import itertools
from my_module import exec_c_with_timeout
import sys

diff_threshold_all = 10 #しきい値

def init_remove_file():
  seg_file_all = 'pretreat_1/seg-*.txt'
  new_seg_file_all = 'pretreat_2/new_seg-*.txt'
  token_file_all = 'pretreat_3/token-*.txt'
  seg_token_file_all = 'pretreat_4/seg_token-*.txt'
  diff_file_all = 'diff/*/*.txt'
  repair_c = 'wrong/repair.c'
  a_out = 'a.out'

  file_list = glob.glob(seg_file_all)
  for file in file_list:
    os.remove(file)

  file_list = glob.glob(new_seg_file_all)
  for file in file_list:
    os.remove(file)

  file_list = glob.glob(token_file_all)
  for file in file_list:
    os.remove(file)

  file_list = glob.glob(seg_token_file_all)
  for file in file_list:
    os.remove(file)

  file_list = glob.glob(diff_file_all)
  for file in file_list:
    os.remove(file)

  if os.path.isfile(repair_c) == True:
    os.remove(repair_c)

  if os.path.isfile(a_out) == True:
    os.remove(a_out)

def input_name():
  name = input('ファイル名を入力 : ')
  prog = 'wrong/' + name + '.c' #修正対象プログラム
  file = 'out/' + name + '-out.txt' #出力ファイル
  if os.path.isfile(file) == True:
    os.remove(file)
  return prog, file

def teba_rewrite(file):
  include = 'norm/include.pt' # #include<stdio.h>を削除
  double_func = 'norm/double_func.pt' # double func1(...)を削除
  int_main = 'norm/int_main.pt' # int main(void){...}を削除
  segment = 'norm/segment.pl' # セグメントの切れ目に改行を挿入
  comment = 'norm/comment.pl' # 連続したスペースとコメントを' 'に置換
  initialize_int = 'norm/initialize_int.pt' # 変数宣言と初期化式を分離(int型)
  initialize_double = 'norm/initialize_double.pt' # 変数宣言と初期化式を分離(double型)
  ineq_for = 'norm/ineq_for.pt' # 不等号の向きを < に統一(for文)
  ineq_for2 = 'norm/ineq_for2.pt' # 不等号の向きを <= に統一(for文)
  ineq_while = 'norm/ineq_while.pt' # 不等号の向きを < に統一(while文)
  ineq_while2 = 'norm/ineq_while2.pt' # 不等号の向きを <= に統一(while文)
  ineq_if = 'norm/ineq_if.pt' # 不等号の向きを < に統一(if文)
  ineq_if2 = 'norm/ineq_if2.pt' # 不等号の向きを <= に統一(if文)
  ineq_ifelse = 'norm/ineq_ifelse.pt' # 不等号の向きを < に統一(ifelse文)
  ineq_ifelse2 = 'norm/ineq_ifelse2.pt' # 不等号の向きを <= に統一(ifelse文)
  ineq_ifelseif1 = 'norm/ineq_ifelseif1.pt' # 不等号の向きを < に統一(if-elseif文)
  ineq_ifelseif2 = 'norm/ineq_ifelseif2.pt'
  ineq_ifelseif3 = 'norm/ineq_ifelseif3.pt'
  ineq_ifelseif4 = 'norm/ineq_ifelseif4.pt'
  ineq_ifelseif5 = 'norm/ineq_ifelseif5.pt'
  ineq_ifelseif6 = 'norm/ineq_ifelseif6.pt'
  ineq_ifelseif7 = 'norm/ineq_ifelseif7.pt'
  ineq_ifelseif8 = 'norm/ineq_ifelseif8.pt'
  ineq_ifelseifelse1 = 'norm/ineq_ifelseifelse1.pt' # 不等号の向きを < に統一(if-elseif-else文)
  ineq_ifelseifelse2 = 'norm/ineq_ifelseifelse2.pt'
  ineq_ifelseifelse3 = 'norm/ineq_ifelseifelse3.pt' 
  ineq_ifelseifelse4 = 'norm/ineq_ifelseifelse4.pt'
  ineq_ifelseifelse5 = 'norm/ineq_ifelseifelse5.pt'
  ineq_ifelseifelse6 = 'norm/ineq_ifelseifelse6.pt'
  ineq_ifelseifelse7 = 'norm/ineq_ifelseifelse7.pt'
  ineq_ifelseifelse8 = 'norm/ineq_ifelseifelse8.pt'
  after_morm_file = 'norm/after_norm.txt' # 正規化処理をした修正対象プログラム

  subprocess.run('cparse.pl ' + file + ' | \
    rewrite.pl -r -p ' + ineq_for + ' | \
      rewrite.pl -r -p ' + ineq_for2 + ' | \
      rewrite.pl -r -p ' + ineq_while + ' | \
        rewrite.pl -r -p ' + ineq_while2 + ' | \
          rewrite.pl -r -p ' + ineq_if + ' | \
            rewrite.pl -r -p ' + ineq_if2 + ' | \
              rewrite.pl -r -p ' + ineq_ifelse + ' | \
                rewrite.pl -r -p ' + ineq_ifelse2 + ' | \
                  rewrite.pl -r -p ' + ineq_ifelseif1 + ' | \
                    rewrite.pl -r -p ' + ineq_ifelseif2 + ' | \
                      rewrite.pl -r -p ' + ineq_ifelseif3 + ' | \
                        rewrite.pl -r -p ' + ineq_ifelseif4 + ' | \
                          rewrite.pl -r -p ' + ineq_ifelseif5 + ' | \
                            rewrite.pl -r -p ' + ineq_ifelseif6 + ' | \
                              rewrite.pl -r -p ' + ineq_ifelseif7 + ' | \
                                rewrite.pl -r -p ' + ineq_ifelseif8 + ' | \
                                  rewrite.pl -r -p ' + ineq_ifelseifelse1 + ' | \
                                    rewrite.pl -r -p ' + ineq_ifelseifelse2 + ' | \
                                      rewrite.pl -r -p ' + ineq_ifelseifelse3 + ' | \
                                        rewrite.pl -r -p ' + ineq_ifelseifelse4 + ' | \
                                          rewrite.pl -r -p ' + ineq_ifelseifelse5 + ' | \
                                            rewrite.pl -r -p ' + ineq_ifelseifelse6 + ' | \
                                              rewrite.pl -r -p ' + ineq_ifelseifelse7 + ' | \
                                                rewrite.pl -r -p ' + ineq_ifelseifelse8 + ' | \
                                                  rewrite.pl -p ' + include + ' | \
                                                    rewrite.pl -p ' + double_func + ' | \
                                                      rewrite.pl -p ' + int_main + ' | \
                                                        rewrite.pl -r -p ' + initialize_int + ' | \
                                                          rewrite.pl -r -p ' + initialize_double + ' | \
                                                            perl ' + segment + ' | \
                                                              perl ' + comment + ' | \
                                                                join-token.pl > ' + after_morm_file, shell = True)

def del_dup_newline():
  file_name = 'norm/after_norm.txt' #正規化処理とセグメント分割の前処理をした修正対象プログラム
  file_str = skip_line_and_return_as_str.skip_line_1(file_name)
  file_str = file_str.replace('else \n', 'else ') #else ifの場合にifの前に挿入した改行を削除
  file_str = file_str.replace('{\n\nfor', '{\nfor') #重複した改行を削除
  file_str = file_str.replace('{\n\nwhile', '{\nwhile') #重複した改行を削除
  f = open(file_name, 'w')
  f.write(file_str)
  f.close()

  return file_name

def split_seg(file1, file2):
  line_num = codecs.open(file2, 'r')
  seg_num = 0
  count = 1
  for line in line_num:
    if line != ' \n':
      if line == ' {\n'or line == '{\n' or line == ' }\n' or line == '}\n': #波括弧を保持
        out = codecs.open('pretreat_1/seg-' + str(count - 1) + ".txt", 'a')
        out.write(line)
      else:
        out = codecs.open('pretreat_1/seg-' + str(count) + ".txt", 'w') #セグメント分割後のファイルを生成
        out.write(line)
        seg_num += 1
        count += 1

  return seg_num

def make_namikakko_list(num):
  list_namikakko = []
  for i in range(num):
    seg_name = 'pretreat_1/seg-' + str(i + 1) + '.txt'
    seg_str = skip_line_and_return_as_str.skip_line_1(seg_name)
    ex_list = re.findall(r'{+', seg_str)
    ex_str = ''.join(ex_list)
    if len(ex_str) == 0:
      ex_list = re.findall(r'}+', seg_str)
      ex_str = ''.join(ex_list)
      if len(ex_str) == 0:
        ex_str = ''
    list_namikakko.append(ex_str)

  return list_namikakko

def del_namikakko(num):
  del_nami = 'norm/del_namikakko.pl' #波括弧を削除
  for i in range(num):
    seg_file = 'pretreat_1/seg-' + str(i + 1) + '.txt'
    new_seg_file = 'pretreat_2/new_seg-' + str(i + 1) + '.txt'
    subprocess.run('cparse.pl ' + seg_file + ' | \
      perl ' + del_nami + ' | \
        join-token.pl > ' + new_seg_file, shell = True)

def split_token(num):
  def kakikae(file):
    file_str = skip_line_and_return_as_str.skip_line_1(file)
    file_str_list = re.findall('<.*>', file_str)
    file_str = ''
    for i in file_str_list:
        file_str += i
    file_str = file_str.replace('<>', '')
    file_str = file_str.replace('< >', '')
    file_str = file_str.replace('<\\n>', '')
    file_str = file_str.replace('<\\t>', '')
    file_str = re.sub('>', '>\n', file_str)
    file_str = file_str.lstrip('<')
    file_str = file_str.replace('\n<', '\n')
    file_str = file_str.replace('>\n', '\n')
    file_str = file_str.replace('\n<', '\n<\n')
    file_str = file_str.replace('<\n=', '<=')
    return file_str

  for i in range(num):
    new_seg_file = 'pretreat_2/new_seg-' + str(i + 1) + '.txt'
    token_file = 'pretreat_3/token-' + str(i + 1) + '.txt'
    seg_token_file = 'pretreat_4/seg_token-' + str(i + 1) + '.txt'
    subprocess.run('cparse.pl ' + new_seg_file + ' > ' + token_file,shell=True)
    f = open(seg_token_file, 'w')
    f.write(kakikae(token_file))
    f.close()

def make_seg_token_list(num):
  seg_token = [''] * num #修正対象プログラムのセグメントファイル名
  seg_token_file_all = 'pretreat_4/seg_token-*.txt'
  file_list = glob.glob(seg_token_file_all)
  file_list = natsorted(file_list)
  for i in range(num):
    seg_token[i] = file_list[i]
  return seg_token

def for_while_id(num, seg_token): #不安定性により、本研究では使用しない
  for_1_index_list = []
  for_2_index_list = [] #forのセグメント番号
  for_3_index_list = []
  for_4_index_list = []
  while_1_index_list = []
  while_2_index_list = [] #whileのセグメント番号
  while_3_index_list = []
  while_4_index_list = []

  for i in range(num):
    search_str = skip_line_and_return_as_str.skip_line_1(seg_token[i])
    pattern = re.match('for|while|', search_str)
    pattern_str = pattern.group()
    if pattern_str == 'for':
      for_2_index_list.append(i)
      for_3_index_list.append(i + 1)
      #前後のセグメントにfor, whileの依存関係があるか判定
      pattern_str = ''
      search_str = skip_line_and_return_as_str.skip_line_1(seg_token[i - 1])
      pattern = re.match('if|else|', search_str)
      pattern_str = pattern.group()
      if len(pattern_str) == 0:
        for_1_index_list.append(i - 1)
      pattern_str = ''
      if len(seg_token) > i + 2:
        search_str = skip_line_and_return_as_str.skip_line_1(seg_token[i + 2])
        pattern = re.match('if|else|', search_str)
        pattern_str = pattern.group()
        if len(pattern_str) == 0:
          for_4_index_list.append(i + 2)
    elif pattern_str == 'while':
      while_2_index_list.append(i)
      while_3_index_list.append(i + 1)
      #前後のセグメントにfor, whileの依存関係があるか判定
      pattern_str = ''
      search_str = skip_line_and_return_as_str.skip_line_1(seg_token[i - 1])
      pattern = re.match('if|else|', search_str)
      pattern_str = pattern.group()
      if len(pattern_str) == 0:
        while_1_index_list.append(i - 1)
      pattern_str = ''
      if len(seg_token) > i + 2:
        search_str = skip_line_and_return_as_str.skip_line_1(seg_token[i + 2])
        pattern = re.match('if|else|', search_str)
        pattern_str = pattern.group()
        if len(pattern_str) == 0:
          while_4_index_list.append(i + 2)
    else:
      pass

  return for_1_index_list, for_2_index_list, for_3_index_list, for_4_index_list, \
    while_1_index_list, while_2_index_list, while_3_index_list, while_4_index_list

def main():
  seg_num_max = 17 #セグメントの最大数
  
  namikakko_start = 'repair/namikakko_start.txt' #波括弧ファイル
  namikakko_end = 'repair/namikakko_end.txt'

  include_text = 'repair/include.txt' #結合ファイル
  int_main_text = 'repair/int_main.txt'

  seg_file_list = [''] * seg_num_max #修正対象プログラムのセグメントごとの差分ファイル名のリスト
  for i in range(seg_num_max):
    seg_file_list[i] = 'diff/' + str(i + 1) + '/*-*.txt'

  correct_list = [''] * seg_num_max #模範解答ファイル名のリスト

  diff_list = [''] * seg_num_max #差分ファイル名のリスト

  sum_list = {} #差分ファイルの行数のリスト
  for i in range(seg_num_max):
    sum_list[i] = []

  init_remove_file() #テキストファイルを削除して初期化

  input_tuple = input_name() #ファイル名を入力
  wrong_prog = input_tuple[0]
  out_file = input_tuple[1]

  teba_rewrite(wrong_prog) #前処理

  after_norm_file = del_dup_newline()
  with open(out_file, 'w') as output_file:
    seg_num = split_seg(output_file, after_norm_file) #セグメント分割

    list_namikakko = make_namikakko_list(seg_num) #波括弧の位置をリストに保持

    del_namikakko(seg_num) #波括弧を削除

    split_token(seg_num) #トークンごとに改行

    seg_token = make_seg_token_list(seg_num) #セグメント分割後のファイル名をリスト化

    #差分生成, 比較
    diff_threshold = [0] * seg_num #差分のしきい値
    for i in range(seg_num):
      diff_flag = 0
      
      if diff_flag == 0:
        seg_token_diff.all(seg_token[i], i + 1) # (seg_token-セグメント番号.txt, セグメント番号)
        correct_file_all = 'correct/all/*/*-*.txt'
        diff_threshold[i] = diff_threshold_all
      elif diff_flag == 1:
        diff_threshold[i] = diff_threshold_all
      elif diff_flag == 2:
        diff_threshold[i] = diff_threshold_all
      elif diff_flag == 3:
        diff_threshold[i] = diff_threshold_all
      elif diff_flag == 4:
        diff_threshold[i] = diff_threshold_all
      elif diff_flag == 5:
        diff_threshold[i] = diff_threshold_all
      elif diff_flag == 6:
        diff_threshold[i] = diff_threshold_all
      elif diff_flag == 7:
        diff_threshold[i] = diff_threshold_all
      elif diff_flag == 8:
        diff_threshold[i] = diff_threshold_all
      diff_list[i] = glob.glob(seg_file_list[i]) #ファイル名をリスト化
      diff_list[i] = natsorted(diff_list[i]) #リストの数字を自然順にソート
      correct_list[i] = glob.glob(correct_file_all) #ファイル名をリスト化
      correct_list[i] = natsorted(correct_list[i]) #リストの数字を自然順にソート
      for j in range(len(diff_list[i])):
        diff_list_str = skip_line_and_return_as_str.skip_line_1(diff_list[i][j])
        if len(diff_list_str) != 0:
          diff_list_str = skip_line_and_return_as_str.skip_line_3(diff_list[i][j]) #差分ファイルの先頭2行を削除
          diff_list_str = diff_list_str.rstrip('\n') #差分ファイル末尾の改行を削除
          f = open(diff_list[i][j], 'w')
          f.write(diff_list_str)
          f.close()
        count = sum([1 for _ in open(diff_list[i][j])]) #行数をカウント
        sum_list[i].append(count) #行数をリスト化
      zip_lists = zip(sum_list[i], diff_list[i], correct_list[i])
      zip_sort = sorted(zip_lists)
      sum_list[i], diff_list[i], correct_list[i] = zip(*zip_sort)

    join_list = [] #結合するファイル名のリスト(修正対象プログラム, 波括弧ファイル)
    for i in range(seg_num):
      join_list.append(seg_token[i]) #ファイル名をリストに追加
      count_start = list_namikakko[i].count('{') #波括弧をリストに追加
      for j in range(count_start):
        join_list.append(namikakko_start)
      count_end = list_namikakko[i].count('}')
      for j in range(count_end):
        join_list.append(namikakko_end)

    sum_flag = []
    sum_flag_count = 0
    for i in range(seg_num):
      if min(sum_list[i]) != 0:
        sum_flag.append(i)
        sum_flag_count += 1
    if sum_flag_count != 2:
      sum_flag.append(-1)
      sum_flag_count += 1
      if sum_flag_count != 2:
        sum_flag.append(-1)

    diff_cand_list = [''] * seg_num #候補の差分ファイル名のリスト
    correct_cand_list = [''] * seg_num #候補の模範解答ファイル名のリスト
    correct_prod_list = [] #模範解答の直積
    diff_prod_list = [] #差分の直積
    correct_prod_sum_list = [] #模範解答の直積の全候補
    diff_prod_sum_list = [] #差分の直積の全候補
    wrong_2_flag = 0

    if sum_flag[1] != -1: #誤りが2セグメント確定
      for i in range(seg_num):
        diff_cand_list[i] = []
        correct_cand_list[i] = []
        for j in range(len(diff_list[i])):
          if i == sum_flag[0]: #差分が1以上
            if sum_list[i][j] <= diff_threshold[i]:
              diff_cand_list[i].append(diff_list[i][j])
              correct_cand_list[i].append(correct_list[i][j])
          elif i == sum_flag[1]: #差分が1以上
            if sum_list[i][j] <= diff_threshold[i]:
              diff_cand_list[i].append(diff_list[i][j])
              correct_cand_list[i].append(correct_list[i][j])
          else: #差分が0
            if sum_list[i][j] == 0:
              diff_cand_list[i].append(diff_list[i][j])
              correct_cand_list[i].append(correct_list[i][j])
      cand_tuple = test_cand.gen_cand(seg_num, correct_cand_list, diff_cand_list)
      correct_prod_list = cand_tuple[0]
      diff_prod_list = cand_tuple[1]
      correct_prod_sum_list.extend(correct_prod_list)
      diff_prod_sum_list.extend(diff_prod_list)

    elif sum_flag[0] != -1: #誤りが1セグメント確定
      for i in range(seg_num):
        diff_cand_list[i] = []
        correct_cand_list[i] = []
        for j in range(len(diff_list[i])):
          if i == sum_flag[0]: #差分が1以上
            if sum_list[i][j] <= diff_threshold[i]:
              diff_cand_list[i].append(diff_list[i][j])
              correct_cand_list[i].append(correct_list[i][j])
          else: #差分が0
            if sum_list[i][j] == 0:
              diff_cand_list[i].append(diff_list[i][j])
              correct_cand_list[i].append(correct_list[i][j])
      cand_tuple = test_cand.gen_cand(seg_num, correct_cand_list, diff_cand_list)
      correct_prod_list = cand_tuple[0]
      diff_prod_list = cand_tuple[1]
      correct_prod_sum_list.extend(correct_prod_list)
      diff_prod_sum_list.extend(diff_prod_list)
      wrong_2_flag = 1

    else: #不明2
      for i in range(seg_num): #不明1を選択
        for j in range(seg_num):
          diff_cand_list[j] = []
          correct_cand_list[j] = []
          for k in range(len(diff_list[j])):
            if j == i:
              if sum_list[j][k] <= diff_threshold[j]:
                diff_cand_list[j].append(diff_list[j][k])
                correct_cand_list[j].append(correct_list[j][k])
            else:
              if sum_list[j][k] == 0:
                diff_cand_list[j].append(diff_list[j][k])
                correct_cand_list[j].append(correct_list[j][k])
        cand_tuple = test_cand.gen_cand(seg_num, correct_cand_list, diff_cand_list)
        correct_prod_list = cand_tuple[0]
        diff_prod_list = cand_tuple[1]
        correct_prod_sum_list.extend(correct_prod_list)
        diff_prod_sum_list.extend(diff_prod_list)
      for i in range(seg_num):
        for j in range(i, seg_num):
          if j == i:
            continue
          for k in range(seg_num):
            diff_cand_list[k] = []
            correct_cand_list[k] = []
            for l in range(len(diff_list[k])):
              if k == i:
                if sum_list[k][l] <= diff_threshold[k]:
                  diff_cand_list[k].append(diff_list[k][l])
                  correct_cand_list[k].append(correct_list[k][l])
              elif k == j:
                if sum_list[k][l] <= diff_threshold[k]:
                  diff_cand_list[k].append(diff_list[k][l])
                  correct_cand_list[k].append(correct_list[k][l])
              else:
                if sum_list[k][l] == 0:
                  diff_cand_list[k].append(diff_list[k][l])
                  correct_cand_list[k].append(correct_list[k][l])
          cand_tuple = test_cand.gen_cand(seg_num, correct_cand_list, diff_cand_list)
          correct_prod_list = cand_tuple[0]
          diff_prod_list = cand_tuple[1]
          correct_prod_sum_list.extend(correct_prod_list)
          diff_prod_sum_list.extend(diff_prod_list)

    seg_token_index_list = [] #修正対象プログラムのセグメントのindex
    temp_list = [''] * seg_num_max #初期化のためにファイル名を保持するリスト
    test_case = skip_line_and_return_as_str.skip_line_1('test_case.txt') #テストケース

    for i in range(len(correct_prod_sum_list)):
      for j in range(len(correct_prod_sum_list[i])):
        if os.path.isfile(seg_token[j]) == False:
          break
        seg_token_index = join_list.index(seg_token[j]) #修正対象プログラムのセグメントのindexを取得
        seg_token_index_list.append(seg_token_index) #リストに追加
        temp_list[j] = join_list[seg_token_index] #tempに保持
        if correct_prod_sum_list[i][j] != '':
          join_list[seg_token_index] = correct_prod_sum_list[i][j] #seg_token[i]を修正済みファイルで置換
      join_seg = ' '.join(join_list) #join_listのファイル名を文字列として結合
      #修正済み修正対象プログラムを生成
      subprocess.run('cat ' + include_text + ' ' + join_seg + ' ' + int_main_text + ' > wrong/repair.c',shell=True)

      if os.path.isfile('a.out') == True:
        os.remove('a.out')
      subprocess.run('cc wrong/repair.c',shell=True)
      if os.path.isfile('a.out') == True:
        repair_prog = exec_c_with_timeout.main() #./a.out
        if repair_prog == 'timeout':
          print(str(i + 1) + ' : ' + 'タイムアウト', file=output_file)
          for j in range(seg_num):
            join_list[seg_token_index_list[j]] = temp_list[j] #初期化
          continue

        #誤りの特定が正しくできたか判定
        if len(repair_prog) != 0: #Cプログラムの実行エラー回避の例外処理
          if test_case == repair_prog:
            end_flag = 1
          else:
            end_flag = 0
        else:
          end_flag = 0
        if end_flag == 1:
          print(str(i + 1) + ' : ' + '成功', file=output_file)
          print('\n', file=output_file)
          for j in range(len(diff_prod_sum_list[i])):
            diff_prod_str = skip_line_and_return_as_str.skip_line_1(diff_prod_sum_list[i][j])
            if len(diff_prod_str) == 0:
              print('セグメント' + str(j + 1) + ' : ' + '誤りなし', file=output_file)
            else:                
              print('セグメント' + str(j + 1) + ' : ' + str(diff_prod_sum_list[i][j]), file=output_file)
              cat_file = subprocess.run('cat ' + str(diff_prod_sum_list[i][j]), shell=True, stdout=subprocess.PIPE)
              cat_file.stdout = str(cat_file.stdout, 'utf-8')
              print(cat_file.stdout, file=output_file)
          sys.exit()
        else:
          print(str(i + 1) + ' : ' + '失敗', file=output_file)
    
        for j in range(seg_num):
          join_list[seg_token_index_list[j]] = temp_list[j] #初期化

      else:
        print(str(i + 1) + ' : ' + 'コンパイルエラー', file=output_file)
        for j in range(seg_num):
          join_list[seg_token_index_list[j]] = temp_list[j] #初期化
  
    mid_count = len(correct_prod_sum_list)
    diff_cand_list = [''] * seg_num #候補の差分ファイル名のリスト
    correct_cand_list = [''] * seg_num #候補の模範解答ファイル名のリスト
    correct_prod_list = [] #模範解答の直積
    diff_prod_list = [] #差分の直積
    correct_prod_sum_list = [] #模範解答の直積の全候補
    diff_prod_sum_list = [] #差分の直積の全候補

    if wrong_2_flag == 0:
      sys.exit()
    elif wrong_2_flag == 1:
      for i in range(seg_num): #不明1
        if i == sum_flag[0]:
          continue
        for j in range(seg_num):
          diff_cand_list[j] = []
          correct_cand_list[j] = []
          for k in range(len(diff_list[j])):
            if j == sum_flag[0]: #差分が1以上
              if sum_list[j][k] <= diff_threshold[j]:
                diff_cand_list[j].append(diff_list[j][k])
                correct_cand_list[j].append(correct_list[j][k])
            else: #差分が0
              if j == i: #不明1を選択
                if sum_list[j][k] <= diff_threshold[j]:
                  diff_cand_list[j].append(diff_list[j][k])
                  correct_cand_list[j].append(correct_list[j][k])
              else:
                if sum_list[j][k] == 0:
                  diff_cand_list[j].append(diff_list[j][k])
                  correct_cand_list[j].append(correct_list[j][k])
        cand_tuple = test_cand.gen_cand(seg_num, correct_cand_list, diff_cand_list)
        correct_prod_list = cand_tuple[0]
        diff_prod_list = cand_tuple[1]
        correct_prod_sum_list.extend(correct_prod_list)
        diff_prod_sum_list.extend(diff_prod_list)
    elif wrong_2_flag == 2:
      for i in range(seg_num):
        for j in range(i, seg_num):
          if j == i:
            continue
          for k in range(seg_num):
            diff_cand_list[k] = []
            correct_cand_list[k] = []
            for l in range(len(diff_list[k])):
              if k == i:
                if sum_list[k][l] <= diff_threshold[k]:
                  diff_cand_list[k].append(diff_list[k][l])
                  correct_cand_list[k].append(correct_list[k][l])
              elif k == j:
                if sum_list[k][l] <= diff_threshold[k]:
                  diff_cand_list[k].append(diff_list[k][l])
                  correct_cand_list[k].append(correct_list[k][l])
              else:
                if sum_list[k][l] == 0:
                  diff_cand_list[k].append(diff_list[k][l])
                  correct_cand_list[k].append(correct_list[k][l])
          cand_tuple = test_cand.gen_cand(seg_num, correct_cand_list, diff_cand_list)
          correct_prod_list = cand_tuple[0]
          diff_prod_list = cand_tuple[1]
          correct_prod_sum_list.extend(correct_prod_list)
          diff_prod_sum_list.extend(diff_prod_list)

    seg_token_index_list = [] #修正対象プログラムのセグメントのindex
    temp_list = [''] * seg_num_max #初期化のためにファイル名を保持するリスト
    test_case = skip_line_and_return_as_str.skip_line_1('test_case.txt') #テストケース

    #修正を適用
    for i in range(len(correct_prod_sum_list)):
      for j in range(len(correct_prod_sum_list[i])):
        if os.path.isfile(seg_token[j]) == False:
          break
        seg_token_index = join_list.index(seg_token[j]) #修正対象プログラムのセグメントのindexを取得
        seg_token_index_list.append(seg_token_index) #リストに追加
        temp_list[j] = join_list[seg_token_index] #tempに保持
        if correct_prod_sum_list[i][j] != '':
          join_list[seg_token_index] = correct_prod_sum_list[i][j] #seg_token[i]を修正済みファイルで置換
      join_seg = ' '.join(join_list) #join_listのファイル名を文字列として結合
      #修正済み修正対象プログラムを生成
      subprocess.run('cat ' + include_text + ' ' + join_seg + ' ' + int_main_text + ' > wrong/repair.c',shell=True)

      if os.path.isfile('a.out') == True:
        os.remove('a.out')
      subprocess.run('cc wrong/repair.c',shell=True)
      if os.path.isfile('a.out') == True:
        repair_prog = exec_c_with_timeout.main() # ./a.out
        if repair_prog == 'timeout':
          print(str(mid_count + i + 1) + ' : ' + 'タイムアウト', file=output_file)
          for j in range(seg_num):
              join_list[seg_token_index_list[j]] = temp_list[j] # 初期化
          continue

        #誤りの特定が正しくできたか判定
        if len(repair_prog) != 0: #Cプログラムの実行エラー回避の例外処理
          if test_case == repair_prog:
            end_flag = 1
          else:
            end_flag = 0
        else:
          end_flag = 0
        if end_flag == 1:
          print(str(mid_count + i + 1) + ' : ' + '成功', file=output_file)
          print('\n', file=output_file)
          for j in range(len(diff_prod_sum_list[i])):
            diff_prod_str = skip_line_and_return_as_str.skip_line_1(diff_prod_sum_list[i][j])
            if len(diff_prod_str) == 0:
              print('セグメント' + str(j + 1) + ' : ' + '誤りなし', file=output_file)
            else:                
              print('セグメント' + str(j + 1) + ' : ' + str(diff_prod_sum_list[i][j]), file=output_file)
              cat_file = subprocess.run('cat ' + str(diff_prod_sum_list[i][j]), shell=True, stdout=subprocess.PIPE)
              cat_file.stdout = str(cat_file.stdout, 'utf-8')
              print(cat_file.stdout, file=output_file)
          break
        else:
          print(str(mid_count + i + 1) + ' : ' + '失敗', file=output_file)
    
        for j in range(seg_num):
          join_list[seg_token_index_list[j]] = temp_list[j] #初期化

      else:
        print(str(mid_count + i + 1) + ' : ' + 'コンパイルエラー', file=output_file)
        for j in range(seg_num):
          join_list[seg_token_index_list[j]] = temp_list[j] #初期化


if __name__ == "__main__":
  main()