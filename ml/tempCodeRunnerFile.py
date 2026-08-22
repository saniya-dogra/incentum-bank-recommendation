        probability = self.model.predict_proba(X)[0][1]
        return round(probability, 4)
