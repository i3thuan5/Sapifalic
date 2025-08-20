Feature: 聖經書寫系統要轉換成原語會書寫系統

Scenario Outline: 系統會補上聖經省略的e

		When 輸入 <聖經書寫>
		Then 輸出 <原語會書寫>

Examples: 開頭連續子音就補e
		| 聖經書寫 | 原語會書寫 |
		| dmak | demak |
		| rmes | remes |

Examples: 詞中的連續子音不補e
		| 聖經書寫 | 原語會書寫 |
		| tamdaw | tamdaw |
		| kahmekan | kahmekan |
		| mahmek | mahmek |

Examples: 去對辭典，補e
		| 聖經書寫 | 原語會書寫 |
		| mihcaan | mihecaan |

Examples: 原本有e不影響
		| 聖經書寫 | 原語會書寫 |
		| tireng | tireng |

Examples: 大寫嘛會補
		| 聖經書寫 | 原語會書寫 |
		| Dmak | Demak |
		| Rmes | Remes |

Examples: 句子
		| 聖經書寫 | 原語會書寫 |
		| Yo ci Hirotiho ko hongti i, | Yo ci Hirotiho ko hongti i, |
