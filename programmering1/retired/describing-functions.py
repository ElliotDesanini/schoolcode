import math
import random

def listdef(inputlist: list = [3,64,12,654,8,54,22,87,6,5,1,34,7,4]) -> None:
    print(f"""\n
    {inputlist}
    - mutable
    - hashable
    - iterable
    - numeric (element dependant)
    - container
    - sequence
    - subscriptable
    [5] {inputlist[5]}
    [5:] {inputlist[5:]}
    [:5] {inputlist[:5]}
    [5:12] {inputlist[5:12]}
    .index(56) {inputlist.index(12)}
    {inputlist.append(7)}
    .append(7) {inputlist}
    len(list) {len(inputlist)}
    sum(list) {sum(inputlist)}
    max(list) {max(inputlist)}
    min(list) {min(inputlist)}
    sorted(list) {sorted(inputlist)}
    {inputlist.sort(reverse=True)}
    .sort(reverse=True) {inputlist}
    {inputlist.sort(reverse=False)}
    .sort(reverse=False) {inputlist}
    .pop() {inputlist.pop()}
    .copy() {inputlist.copy()}
    .pop(87) {inputlist.pop(7)}
    {inputlist.extend([1,2,3])}
    .extend[1,2,3] {inputlist}
    {inputlist.insert(4, 111111)}
    .insert(3,111111) {inputlist}
    {inputlist.remove(4)}
    .remove(4) {inputlist}")
    {inputlist.clear()}
    .clear() {inputlist}\n
""")


def strdef(inputstr: str = " abcde ABCDE 12345 #%& catdogR") -> None:
    print(f"""\n
    {inputstr}
    - immutable
    - non-hashable
    - iterable
    - non-numeric
    - sequence
    - subscriptable
    [5] {inputstr[5]}
    [5:] {inputstr[5:]}
    [:5] {inputstr[:5]}
    [5:12] {inputstr[5:12]}
    .index(\"A\") {inputstr.index("A")}
    .count(\"c\") {inputstr.count("c")}
    .lower() {inputstr.lower()}
    .upper() {inputstr.upper()}
    .title() {inputstr.title()}
    .strip() {inputstr.strip()}
    .strip(\"T\") {inputstr.strip("R")}
    .replace(\"B\", \"A\") {inputstr.replace("B", "A")}
    .split() {inputstr.split()}
    .split(\"d\") {inputstr.split("d")}
    .isalnum() {inputstr.isalnum()}
    .isalpha() {inputstr.isalpha()}
    .isdigit() {inputstr.isdigit()}\n
""")


def intdef(inputint: int = 255) -> None:
    print(f"""
    {inputint}
    - numeric
    - immutable
    - non-sequence
    - non-subscriptable
    - non-iterable
    - signed vs unsigned
    - arbitrary vs non-arbitrary precision
    .bit_length() {inputint.bit_length()}
    .to_bytes(2, byteorder='big') {inputint.to_bytes(2, byteorder='big')}
    
""")

listdef()