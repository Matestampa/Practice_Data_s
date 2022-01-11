#--------quick sort(original)------------vamosssssssss salio el recursivo(1/2 copiado)--------------------------
from random import randint
import time
lista=2463, 2464, 2464, 2465, 2470, 2472, 2480, 2484, 2488, 2493, 2496, 2503, 2504, 2505, 2507, 2507, 2512, 2523, 2532, 2534, 2537, 2538, 2538, 2539, 2540, 2547, 2550, 2551, 2555, 2556, 2558, 2559, 2560, 2571, 2579, 2580, 2584, 2590, 2590, 2594, 2599, 2621, 2624, 2628, 2629, 2631, 2634, 2635, 2640, 2645, 2653, 2654, 2655, 2655, 2656, 2657, 2658, 2663, 2666, 2667, 2674, 2675, 2682, 2693, 2699, 2705, 2710, 2720, 2720, 2724, 2725, 2725, 2725, 2726, 2730, 2733, 2733, 2739, 2741, 2759, 2770, 2773, 2774, 2780, 2781, 2781, 2787, 2789, 2791, 2797, 2800, 2802, 2806, 2815, 2818, 2832, 2836, 2843, 2844, 2846, 2847, 2850, 2851, 2862, 2863, 2868, 2870, 2884, 2885, 2898, 2898, 2902, 2910, 2912, 2932, 2935, 2937, 2937, 2941, 2943, 2947, 2949, 2950, 2957, 2969, 2969, 2971, 2974, 2975, 2975, 2977, 2979, 2980, 2982, 2982, 2987, 3000, 3001, 3001, 3002, 3003, 3015, 3018, 3019, 3020, 3021, 3025, 3026, 3027, 3027, 3034, 3039, 3044, 3045, 3046, 3050, 3051, 3056, 3060, 3064, 3068, 3072, 3073, 3075, 3079, 3081, 3092, 3095, 3095, 3098, 3098, 3099, 3103, 3108, 3109, 3111, 3112, 3114, 3117, 3120, 3125, 3140, 3142, 3143, 3146, 3146, 3147, 3152, 3156, 3158, 3166, 3169, 3172, 3173, 3180, 3182, 3183, 3187, 3189, 3190, 3194, 3210, 3211, 3212, 3218, 3222, 3223, 3223, 3223, 3227, 3234, 3243, 3246, 3265, 3266, 3289, 3290, 3290, 3292, 3294, 3295, 3295, 3303, 3309, 3314, 3324, 3325, 3329, 3330, 3338, 3340, 3350, 3350, 3358, 3359, 3362, 3364, 3367, 3370, 3371, 3371, 3377, 3379, 3386, 3388, 3393, 3394, 3395, 3395, 3401, 3404, 3411, 3412, 3423, 3431, 3435, 3436, 3439, 3445, 3455, 3459, 3460, 3462, 3463, 3467, 3470, 3472, 3477, 3495, 3495, 3496, 3496, 3504, 3506, 3510, 3515, 3519, 3525, 3525, 3526, 3529, 3543, 3547, 3553, 3554, 3554, 3572, 3572, 3573, 3577, 3579, 3581, 3597, 3599, 3601, 3603, 3618, 3620, 3620, 3628, 3638, 3641, 3648, 3651, 3653, 3653, 3657, 3658, 3665, 3666, 3669, 3674, 3680, 3684, 3694, 3695, 3696, 3698, 3699, 3704, 3706, 3707, 3708, 3713, 3713, 3714, 3717, 3718, 3720, 3721, 3722, 3728, 3735, 3744, 3750, 3769, 3770, 3773, 3779, 3780, 3783, 3783, 3785, 3787, 3790, 3792, 3793, 3794, 3795, 3803, 3822, 3828, 3837, 3843, 3845, 3859, 3866, 3868, 3871, 3874, 3877, 3885, 3899, 3905, 3907, 3909, 3918, 3922, 3924, 3924, 3928, 3932, 3933, 3933, 3937, 3940, 3941, 3944, 3947, 3963, 3964, 3976, 3978, 3983, 3984, 3990, 3993, 3997, 3999]


def partition(lista,s,f):
    
    pivot=f
    p=lista[pivot]
    i=s
    j=s
    while j!=f:
          if lista[j]<p:
             lista[j],lista[i]=lista[i],lista[j]
             i+=1
             j+=1
          else:
             j+=1
    lista[j],lista[i]=lista[i],lista[j]
    #mostar(lista)
    return i


def recursion(lista,s,f):
  if s>=f: 
     #print("listo")
     return lista[s:f+1]
     
  else:   
     index=partition(lista,s,f)
     #print(index,"index")
     #print(lista)
     return recursion(lista,s,index-1) + [lista[index]] + recursion(lista,index+1,f)


inicio=time.time()
final=time.time()
print(recursion(lista,0,999))
print(final-inicio)