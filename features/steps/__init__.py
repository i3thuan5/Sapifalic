from behave import when, then
from sapifalic import bible2ilrdf


@when('輸入 {bible}')
def step_impl(context, bible):
    context.bible = bible


@then(u'輸出 {ilrdf}')
def step_impl(context, ilrdf):
    assert bible2ilrdf(context.bible) == ilrdf
