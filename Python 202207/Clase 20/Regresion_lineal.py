#!/usr/bin/env python
# coding: utf-8

# ## Otras funciones

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
aux1 = np.arange(-3,3,0.1)
aux2 = np.arange(1,4,0.05)
aux3 = 30 + 2*aux1 - 1.5*np.log(aux2) + 2*np.random.normal(size=len(aux1))
Datos = pd.DataFrame({'Y': aux3, 'X1': aux1, 'X2': aux2})
Datos.head(10)


# In[2]:


modelo = smf.ols('Y ~ X1 + np.log(X2)', data = Datos)
result = modelo.fit()
result.summary()


# In[3]:


result.conf_int()


# In[4]:


result.resid


# In[5]:


from statsmodels.sandbox.regression.predstd import wls_prediction_std as IC


# In[6]:


distanc, low, up = IC(result)
intervalos = pd.DataFrame({'Intervalo inferior': low, 'Predicción': result.predict(), 'Intervalo superior': up, 'Error': distanc})
intervalos


# In[7]:


plt.errorbar(intervalos.index, intervalos['Predicción'], yerr=intervalos['Error'])
plt.xlabel('Observación')
plt.ylabel('Y')
plt.show()


# In[8]:


plt.errorbar(intervalos.index, intervalos['Predicción'], yerr=intervalos['Error'])
plt.scatter(Datos.index, Datos['Y'], c='r')
plt.xlabel('Observación')
plt.ylabel('Y')
plt.show()


# In[9]:


plt.plot(intervalos.index, intervalos['Predicción'],
        intervalos.index, intervalos['Intervalo inferior'], 'r',
        intervalos.index, intervalos['Intervalo superior'], 'r')
plt.legend(['Predicción', 'Intervalos'])
plt.xlabel('Observación')
plt.ylabel('Y')
plt.show()


# In[10]:


intervalos[['Predicción', 'Intervalo inferior', 'Intervalo superior']].plot(color=['b', 'r', 'r'], legend=False)
plt.legend(['Predicción', 'Intervalos'])
plt.xlabel('Observación')
plt.ylabel('Y')
plt.show()

