from behave import when, then
from sapifalic import bible2ilrdf


@when('輸入 {bible}')
def 輸入(context, bible):
    context.bible = bible


@then('輸出 {ilrdf}')
def 輸出(context, ilrdf):
    assert bible2ilrdf(context.bible) == ilrdf, (
        '結果是：' + bible2ilrdf(context.bible)
    )
