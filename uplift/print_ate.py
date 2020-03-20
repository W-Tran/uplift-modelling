def visit_rate_ate(df, test_set=False):
    if test_set:
        treatment_visit_rate = df[df.Treatment == 1].Outcome.mean() * 100
        control_visit_rate = df[df.Treatment == 0].Outcome.mean() * 100
        average_treatment_effect = treatment_visit_rate - control_visit_rate
        print("Test set visit rate uplift: {:.2f}%".format(average_treatment_effect))
        return average_treatment_effect
    else:
        mens = df[df.segment == "Mens E-Mail"].visit.mean() * 100
        womens = df[df.segment == "Womens E-Mail"].visit.mean() * 100
        control = df[df.segment == "No E-Mail"].visit.mean() * 100
        print("Men's E-Mail visit rate: {:.2f}%".format(mens))
        print("Women's E-Mail visit rate: {:.2f}%".format(womens))
        print("Control E-mail visit Rate: {:.2f}%".format(control))
        print("---------------------------------")
        print("Men's visit rate uplift: {:.2f}%".format(mens - control))
        print("Women's visit rate uplift: {:.2f}%".format(womens - control))


def conversion_rate_ate(df):
    mens = df[df.segment == "Mens E-Mail"].conversion.mean() * 100
    womens = df[df.segment == "Womens E-Mail"].conversion.mean() * 100
    control = df[df.segment == "No E-Mail"].conversion.mean() * 100
    print("Men's E-Mail conversion rate: {:.2f}%".format(mens))
    print("Women's E-Mail conversion rate: {:.2f}%".format(womens))
    print("Control E-mail conversion Rate: {:.2f}%".format(control))
    print("---------------------------------")
    print("Men's conversion rate uplift: {:.2f}%".format(mens - control))
    print("Women's conversion rate uplift: {:.2f}%".format(womens - control))


def spending_ate(df):
    mens = df[df.segment == "Mens E-Mail"].spend.mean()
    womens = df[df.segment == "Womens E-Mail"].spend.mean()
    control = df[df.segment == "No E-Mail"].spend.mean()
    print("Men's E-Mail spending: ${:.2f}".format(mens))
    print("Women's E-Mail spending: ${:.2f}".format(womens))
    print("Control E-mail spending: ${:.2f}".format(control))
    print("---------------------------------")
    print("Men's spending uplift: ${:.2f}".format(mens - control))
    print("Women's spending uplift: ${:.2f}".format(womens - control))


def spend_given_purchase(df):
    print("Men's average spend given purchase: ${:.2f}".format(
        df[(df.conversion == 1) & (df.segment == 'Mens E-Mail')].spend.mean()))
    print("Women's average spend given purchase: ${:.2f}".format(
        df[(df.conversion == 1) & (df.segment == 'Womens E-Mail')].spend.mean()))
    print("Control average spend given purchase: ${:.2f}".format(
        df[(df.conversion == 1) & (df.segment == 'No E-Mail')].spend.mean()))


def purchase_given_visit(df):
    print("Men's purchase rate given visit: {:.2f}%".format(100 * (
            len(df[(df.conversion == 1) & (df.segment == 'Mens E-Mail')]) / len(
        df[(df.visit == 1) & (df.segment == 'Mens E-Mail')]))))
    print("Women's purchase rate given visit: {:.2f}%".format(100 * (
            len(df[(df.conversion == 1) & (df.segment == 'Womens E-Mail')]) / len(
        df[(df.visit == 1) & (df.segment == 'Womens E-Mail')]))))
    print("Control purchase rate given visit: {:.2f}%".format(100 * (
            len(df[(df.conversion == 1) & (df.segment == 'No E-Mail')]) / len(
        df[(df.visit == 1) & (df.segment == 'No E-Mail')]))))


def visit_rate(df):
    print("Men's visit rate: {:.2f}%".format(
        100 * (len(df[(df.visit == 1) & (df.segment == 'Mens E-Mail')]) / len(df[(df.segment == 'Mens E-Mail')]))))
    print("Women's visit rate: {:.2f}%".format(
        100 * (len(df[(df.visit == 1) & (df.segment == 'Womens E-Mail')]) / len(df[(df.segment == 'Womens E-Mail')]))))
    print("Control visit rate: {:.2f}%".format(
        100 * (len(df[(df.visit == 1) & (df.segment == 'No E-Mail')]) / len(df[(df.segment == 'No E-Mail')]))))


def spend_per_head(df):
    print("Men's mean spend: ${:.2f}".format(df[(df.segment == 'Mens E-Mail')].spend.mean()))
    print("Women's mean spend: ${:.2f}".format(df[(df.segment == 'Womens E-Mail')].spend.mean()))
    print("Control mean spend: ${:.2f}".format(df[(df.segment == 'No E-Mail')].spend.mean()))
