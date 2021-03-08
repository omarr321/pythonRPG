def sortList(itemList, arrInt):
        itemL = list()
        for x in itemList:
            itemL.append(x)

        if len(itemL) == 1:
            return itemL
        elif len(itemL) == 0:
            return list()
        
        top = list()
        bottom = list()

        count = 2
        for x in itemList:
            if count % 2 == 1:
                top.append(x)
            else:
                bottom.append(x)
            count = count + 1
        
        top = sortList(top, 0)
        bottom = sortList(bottom, 0)

        totalLen = len(top) + len(bottom)
        together = list()
        for _ in range (0, totalLen):
            if len(top) == 0:
                together.append(bottom.pop())
            elif len(bottom) == 0:
                together.append(top.pop())
            else:
                if top[0][arrInt].toString() == bottom[0][arrInt].toString():
                    together.append(top[0])
                    top.remove(top[0])
                elif top[0][arrInt].toString() > bottom[0][arrInt].toString():
                    together.append(bottom[0])
                    bottom.remove(bottom[0])
                else:
                    together.append(top[0])
                    top.remove(top[0])
        return together